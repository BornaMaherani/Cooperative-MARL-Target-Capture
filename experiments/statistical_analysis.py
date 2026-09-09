import os
import glob
import csv
import math
from collections import defaultdict
import matplotlib.pyplot as plt

import configs.evaluation_config as cfg

def calculate_mean_std(data_list):
    if not data_list:
        return 0.0, 0.0
    n = len(data_list)
    mean = sum(data_list) / n
    if n <= 1:
        return mean, 0.0
    variance = sum((x - mean) ** 2 for x in data_list) / (n - 1)
    std = math.sqrt(variance)
    return mean, std

def read_raw_results(filepath):
    results = []
    if not os.path.exists(filepath):
        return results
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            results.append(row)
    return results

def aggregate_and_plot():
    os.makedirs(cfg.SUMMARIES_DIR, exist_ok=True)
    os.makedirs(cfg.PLOTS_DIR, exist_ok=True)
    
    summary_data = []
    csv_files = glob.glob(os.path.join(cfg.RAW_RESULTS_DIR, "*_results.csv"))
    
    # Variables for plotting
    methods = []
    capture_means = []
    capture_errs = []
    length_means = []
    length_errs = []
    reward_means = []
    reward_errs = []
    
    for fpath in sorted(csv_files):
        data = read_raw_results(fpath)
        if not data:
            continue
            
        method_name = data[0]['method']
        
        # Group by training_seed
        seed_metrics = defaultdict(lambda: {"cap": [], "len": [], "rew": [], "time": []})
        for row in data:
            seed = int(row['training_seed'])
            seed_metrics[seed]["cap"].append(int(row['captured']))
            seed_metrics[seed]["len"].append(int(row['episode_length']))
            seed_metrics[seed]["rew"].append(float(row['episode_reward']))
            if row['capture_time']:
                seed_metrics[seed]["time"].append(int(row['capture_time']))
                
        # Calculate per-seed averages
        per_seed_cap_rates = []
        per_seed_avg_len = []
        per_seed_avg_rew = []
        per_seed_avg_time = []
        
        for seed, metrics in seed_metrics.items():
            cap_rate = sum(metrics["cap"]) / len(metrics["cap"])
            avg_len = sum(metrics["len"]) / len(metrics["len"])
            avg_rew = sum(metrics["rew"]) / len(metrics["rew"])
            
            per_seed_cap_rates.append(cap_rate)
            per_seed_avg_len.append(avg_len)
            per_seed_avg_rew.append(avg_rew)
            
            if metrics["time"]:
                avg_time = sum(metrics["time"]) / len(metrics["time"])
                per_seed_avg_time.append(avg_time)
                
        # Calculate mean/std across seeds
        cr_m, cr_s = calculate_mean_std(per_seed_cap_rates)
        len_m, len_s = calculate_mean_std(per_seed_avg_len)
        rew_m, rew_s = calculate_mean_std(per_seed_avg_rew)
        time_m, time_s = calculate_mean_std(per_seed_avg_time) if per_seed_avg_time else (float('nan'), 0.0)
        
        summary_data.append({
            "method": method_name,
            "capture_rate_mean": cr_m,
            "capture_rate_std": cr_s,
            "episode_length_mean": len_m,
            "episode_length_std": len_s,
            "capture_time_mean": time_m,
            "capture_time_std": time_s,
            "episode_reward_mean": rew_m,
            "episode_reward_std": rew_s,
        })
        
        methods.append(method_name)
        capture_means.append(cr_m)
        capture_errs.append(cr_s)
        length_means.append(len_m)
        length_errs.append(len_s)
        reward_means.append(rew_m)
        reward_errs.append(rew_s)

    # Save CSV
    if summary_data:
        keys = summary_data[0].keys()
        with open(os.path.join(cfg.SUMMARIES_DIR, "comparison_summary.csv"), 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(summary_data)
            
    # Generate Plots
    if methods:
        _plot_bar(methods, capture_means, capture_errs, "Capture Rate", "Capture Rate Comparison", "capture_rate_comparison.png", ylim=(0, 1))
        _plot_bar(methods, length_means, length_errs, "Episode Length", "Episode Length Comparison", "episode_length_comparison.png")
        _plot_bar(methods, reward_means, reward_errs, "Episode Reward", "Episode Reward Comparison", "reward_comparison.png")

def _plot_bar(categories, means, errs, ylabel, title, filename, ylim=None):
    plt.figure(figsize=(10, 6))
    x_pos = range(len(categories))
    plt.bar(x_pos, means, yerr=errs, align='center', alpha=0.7, ecolor='black', capsize=10)
    plt.ylabel(ylabel)
    plt.xticks(x_pos, categories, rotation=15)
    plt.title(title)
    if ylim:
        plt.ylim(ylim)
    plt.tight_layout()
    plt.savefig(os.path.join(cfg.PLOTS_DIR, filename))
    plt.close()

if __name__ == "__main__":
    aggregate_and_plot()
