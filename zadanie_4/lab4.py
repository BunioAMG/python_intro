import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pymcdm.methods import TOPSIS, SPOTIS, VIKOR
from pymcdm.normalizations import minmax_normalization
from pymcdm.weights import entropy_weights


def prepare_data():
    """
    Creates a realistic decision matrix for selecting a business laptop.
    """
    matrix = np.array([
        [3400, 3200, 8, 1.4, 512],    # A1
        [4200, 3600, 12, 1.7, 1024],  # A2
        [3900, 3100, 9, 1.5, 512],    # A3
        [4600, 4000, 11, 1.8, 2048]   # A4
    ])
    alternatives = ['A1', 'A2', 'A3', 'A4']
    criteria = ['Price (PLN)', 'Performance', 'Battery (h)', 'Weight (kg)', 'Storage (GB)']
    types = np.array([-1, 1, 1, -1, 1])  # Minimize: Price, Weight; Maximize: others
    return matrix, alternatives, criteria, types


def calculate_entropy_weights(matrix):
    """
    Calculates criteria weights using the entropy method.
    """
    return entropy_weights(matrix)


def run_methods(matrix, norm_matrix, weights, types):
    """
    Executes decision-making methods: TOPSIS, SPOTIS, VIKOR.
    """
    results = {}

    # TOPSIS
    results['TOPSIS'] = TOPSIS()(norm_matrix, weights, types)

    # SPOTIS
    bounds = np.column_stack((np.min(matrix, axis=0), np.max(matrix, axis=0)))
    results['SPOTIS'] = SPOTIS(bounds)(matrix, weights, types)

    # VIKOR
    results['VIKOR'] = VIKOR()(norm_matrix, weights, types)

    return results


def make_result_table(results, alternatives):
    """
    Creates a table with scores and rankings for each method.
    """
    df = pd.DataFrame(results, index=alternatives)
    df['Rank_TOPSIS'] = df['TOPSIS'].rank(ascending=False).astype(int)
    df['Rank_SPOTIS'] = df['SPOTIS'].rank(ascending=True).astype(int)
    df['Rank_VIKOR'] = df['VIKOR'].rank(ascending=True).astype(int)
    return df


def plot_rankings(df):
    """
    Visualizes rankings as a bar chart.
    """
    df[['Rank_TOPSIS', 'Rank_SPOTIS', 'Rank_VIKOR']].plot(kind='bar')
    plt.title('Comparison of Rankings by MCDM Methods')
    plt.ylabel('Ranking Position (1 = best)')
    plt.xlabel('Alternative')
    plt.xticks(rotation=0)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()


def main():
    # 1. Input data
    matrix, alternatives, criteria, types = prepare_data()

    # 2. Display decision matrix
    print("\nDecision Matrix:")
    df_matrix = pd.DataFrame(matrix, columns=criteria, index=alternatives)
    print(df_matrix)

    # 3. Calculate entropy-based weights
    weights = calculate_entropy_weights(matrix)
    print("\nEntropy Weights:", np.round(weights, 4))

    # 4. Normalize decision matrix
    norm_matrix = minmax_normalization(matrix)

    # 5. Run decision-making methods
    results = run_methods(matrix, norm_matrix, weights, types)

    # 6. Display results and rankings
    df = make_result_table(results, alternatives)
    print("\nResults and Rankings:")
    print(df)

    # 7. Plot rankings
    plot_rankings(df)


if __name__ == "__main__":
    main()

