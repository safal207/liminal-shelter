"""Visualization module for Liminal Shelter emotional data."""

import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Dict, Any, Optional
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Set style for beautiful plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")


class EmotionalVisualizer:
    """Creates visualizations for emotional growth and shelter metrics."""

    def __init__(self):
        """Initialize the visualizer with styling."""
        self.colors = {
            'trust': '#4CAF50',      # Green
            'joy': '#FFC107',        # Amber
            'gratitude': '#9C27B0',  # Purple
            'care': '#2196F3',       # Blue
            'growth': '#FF5722',     # Deep Orange
            'crisis': '#F44336',     # Red
            'recovery': '#00BCD4'    # Cyan
        }

    def plot_trust_growth(self, trust_history: List[float],
                         time_points: Optional[List[str]] = None,
                         title: str = "Trust Growth Journey") -> plt.Figure:
        """Plot trust level progression over time."""
        fig, ax = plt.subplots(figsize=(12, 6))

        if time_points is None:
            time_points = [f"T{i+1}" for i in range(len(trust_history))]

        # Plot trust line
        ax.plot(time_points, trust_history, 'o-', color=self.colors['trust'],
                linewidth=3, markersize=8, label='Trust Level')

        # Add trend line
        if len(trust_history) > 2:
            z = np.polyfit(range(len(trust_history)), trust_history, 2)
            p = np.poly1d(z)
            trend_x = np.linspace(0, len(trust_history)-1, 100)
            ax.plot(trend_x, p(trend_x), '--', color=self.colors['growth'],
                   alpha=0.7, label='Growth Trend')

        # Styling
        ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Time Points', fontsize=12)
        ax.set_ylabel('Trust Level', fontsize=12)
        ax.grid(True, alpha=0.3)
        ax.legend(fontsize=10)

        # Set y-axis limits
        ax.set_ylim(0, 1.1)

        plt.tight_layout()
        return fig

    def plot_emotional_distribution(self, emotions: Dict[str, float],
                                  title: str = "Emotional State Distribution") -> plt.Figure:
        """Create a radar chart of emotional states."""
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))

        # Prepare data
        emotion_names = list(emotions.keys())
        emotion_values = list(emotions.values())

        # Create angles for radar chart
        angles = np.linspace(0, 2 * np.pi, len(emotion_names), endpoint=False).tolist()
        emotion_values += emotion_values[:1]  # Close the circle
        angles += angles[:1]

        # Plot
        ax.fill(angles, emotion_values, color=self.colors['joy'], alpha=0.25)
        ax.plot(angles, emotion_values, 'o-', color=self.colors['joy'],
               linewidth=2, label='Emotional Intensity')

        # Labels
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(emotion_names, fontsize=10)
        ax.set_ylim(0, 1)
        ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
        ax.grid(True)

        plt.tight_layout()
        return fig

    def plot_care_exchange_heatmap(self, care_matrix: List[List[float]],
                                  guardian_names: List[str],
                                  seedling_names: List[str],
                                  title: str = "Care Exchange Intensity") -> plt.Figure:
        """Create heatmap of care exchanges between guardians and seedlings."""
        fig, ax = plt.subplots(figsize=(10, 8))

        # Create heatmap
        im = ax.imshow(care_matrix, cmap='YlOrRd', aspect='auto')

        # Add labels
        ax.set_xticks(np.arange(len(seedling_names)))
        ax.set_yticks(np.arange(len(guardian_names)))
        ax.set_xticklabels(seedling_names, rotation=45, ha='right')
        ax.set_yticklabels(guardian_names)

        # Add colorbar
        cbar = ax.figure.colorbar(im, ax=ax, shrink=0.8)
        cbar.ax.set_ylabel("Care Intensity", rotation=-90, va="bottom")

        # Add text annotations
        for i in range(len(guardian_names)):
            for j in range(len(seedling_names)):
                text = ax.text(j, i, '.1f',
                             ha="center", va="center", color="black", fontsize=8)

        ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
        plt.tight_layout()
        return fig

    def plot_shelter_climate_timeline(self, climate_history: List[Dict[str, Any]],
                                     title: str = "Shelter Climate Evolution") -> plt.Figure:
        """Plot shelter climate changes over time."""
        fig, ax = plt.subplots(figsize=(14, 8))

        if not climate_history:
            ax.text(0.5, 0.5, 'No climate data available',
                   ha='center', va='center', transform=ax.transAxes)
            return fig

        # Extract data
        times = [entry.get('timestamp', i) for i, entry in enumerate(climate_history)]
        trust_levels = [entry.get('trust_level', 0.5) for entry in climate_history]
        emotional_states = [entry.get('emotional_state', 'neutral') for entry in climate_history]

        # Plot trust levels
        ax.plot(times, trust_levels, 'o-', color=self.colors['trust'],
               linewidth=3, markersize=6, label='Average Trust')

        # Add emotional state markers
        emotion_colors = {
            'joy': self.colors['joy'],
            'gratitude': self.colors['gratitude'],
            'crisis': self.colors['crisis'],
            'recovery': self.colors['recovery'],
            'neutral': '#9E9E9E'
        }

        for i, (time, emotion) in enumerate(zip(times, emotional_states)):
            color = emotion_colors.get(emotion, '#9E9E9E')
            ax.scatter(time, trust_levels[i], c=color, s=100, alpha=0.7, edgecolors='black')

        # Styling
        ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Time', fontsize=12)
        ax.set_ylabel('Trust Level', fontsize=12)
        ax.grid(True, alpha=0.3)
        ax.set_ylim(0, 1.1)

        # Add legend
        legend_elements = [plt.Line2D([0], [0], marker='o', color='w',
                                    markerfacecolor=color, markersize=10, label=emotion)
                          for emotion, color in emotion_colors.items()]
        ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1.05, 1))

        plt.tight_layout()
        return fig

    def plot_growth_milestones(self, milestones: List[Dict[str, Any]],
                              title: str = "Growth Milestones") -> plt.Figure:
        """Create a timeline of growth milestones."""
        fig, ax = plt.subplots(figsize=(12, 6))

        if not milestones:
            ax.text(0.5, 0.5, 'No milestone data available',
                   ha='center', va='center', transform=ax.transAxes)
            return fig

        # Extract milestone data
        times = [m.get('time', i) for i, m in enumerate(milestones)]
        trust_levels = [m.get('trust_level', 0.5) for m in milestones]
        descriptions = [m.get('description', '') for m in milestones]

        # Plot milestones
        ax.plot(times, trust_levels, 'o--', color=self.colors['growth'],
               alpha=0.5, linewidth=2)

        # Add milestone markers and labels
        for i, (time, trust, desc) in enumerate(zip(times, trust_levels, descriptions)):
            ax.scatter(time, trust, s=150, c=self.colors['joy'],
                      edgecolors='black', linewidth=2, alpha=0.8)

            # Add description label
            ax.annotate(desc[:30] + ('...' if len(desc) > 30 else ''),
                       (time, trust),
                       xytext=(10, 10), textcoords='offset points',
                       bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8),
                       fontsize=9)

        # Styling
        ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Time Points', fontsize=12)
        ax.set_ylabel('Trust Level', fontsize=12)
        ax.grid(True, alpha=0.3)
        ax.set_ylim(0, 1.1)

        plt.tight_layout()
        return fig

    def create_comprehensive_report(self, trust_history: List[float],
                                  emotional_states: Dict[str, float],
                                  care_matrix: List[List[float]],
                                  climate_history: List[Dict[str, Any]],
                                  guardian_names: List[str],
                                  seedling_names: List[str],
                                  output_file: str = "liminal_shelter_report.png"):
        """Create a comprehensive visualization report."""
        fig = plt.figure(figsize=(16, 12))

        # Create subplots
        gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

        # 1. Trust Growth (top left)
        ax1 = fig.add_subplot(gs[0, 0])
        ax1.plot(range(len(trust_history)), trust_history, 'o-',
                color=self.colors['trust'], linewidth=2)
        ax1.set_title('Trust Growth', fontweight='bold')
        ax1.set_ylim(0, 1.1)
        ax1.grid(True, alpha=0.3)

        # 2. Emotional Distribution (top middle)
        ax2 = fig.add_subplot(gs[0, 1])
        emotions = list(emotional_states.keys())
        values = list(emotional_states.values())
        bars = ax2.bar(range(len(emotions)), values,
                      color=[self.colors.get(e, '#9E9E9E') for e in emotions])
        ax2.set_xticks(range(len(emotions)))
        ax2.set_xticklabels(emotions, rotation=45, ha='right')
        ax2.set_title('Emotional States', fontweight='bold')
        ax2.set_ylim(0, 1)

        # 3. Care Heatmap (top right)
        ax3 = fig.add_subplot(gs[0, 2])
        if care_matrix:
            im = ax3.imshow(care_matrix, cmap='YlOrRd', aspect='auto')
            ax3.set_xticks(range(len(seedling_names)))
            ax3.set_yticks(range(len(guardian_names)))
            ax3.set_xticklabels([s[:8] + '...' for s in seedling_names], rotation=45, ha='right')
            ax3.set_yticklabels([g[:8] + '...' for g in guardian_names])
            ax3.set_title('Care Intensity', fontweight='bold')

        # 4. Climate Timeline (bottom span)
        ax4 = fig.add_subplot(gs[1:, :])
        if climate_history:
            times = range(len(climate_history))
            trust_levels = [c.get('trust_level', 0.5) for c in climate_history]
            ax4.plot(times, trust_levels, 'o-', color=self.colors['care'],
                    linewidth=3, markersize=6)
            ax4.fill_between(times, trust_levels, alpha=0.3, color=self.colors['care'])
            ax4.set_title('Climate Evolution Timeline', fontsize=14, fontweight='bold')
            ax4.set_xlabel('Time Points')
            ax4.set_ylabel('Trust Level')
            ax4.grid(True, alpha=0.3)
            ax4.set_ylim(0, 1.1)

        # Main title
        fig.suptitle('🌸 Liminal Shelter - Comprehensive Emotional Report',
                    fontsize=16, fontweight='bold', y=0.98)

        plt.tight_layout()
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close()

        print(f"📊 Comprehensive report saved to: {output_file}")
        return output_file


def demo_visualizations():
    """Demo function showing all visualization types."""
    visualizer = EmotionalVisualizer()

    # Sample data
    trust_history = [0.2, 0.35, 0.48, 0.62, 0.75, 0.83, 0.91, 0.95]
    emotional_states = {'joy': 0.8, 'gratitude': 0.9, 'trust': 0.85, 'care': 0.75}
    care_matrix = [[0.8, 0.6], [0.9, 0.7], [0.5, 0.8]]
    climate_history = [
        {'trust_level': 0.3, 'emotional_state': 'crisis'},
        {'trust_level': 0.5, 'emotional_state': 'recovery'},
        {'trust_level': 0.7, 'emotional_state': 'joy'},
        {'trust_level': 0.8, 'emotional_state': 'gratitude'}
    ]

    print("🎨 Creating visualizations...")

    # Create individual plots
    fig1 = visualizer.plot_trust_growth(trust_history)
    fig1.savefig('trust_growth.png', dpi=150, bbox_inches='tight')
    plt.close(fig1)
    print("✅ Trust growth chart created")

    fig2 = visualizer.plot_emotional_distribution(emotional_states)
    fig2.savefig('emotional_distribution.png', dpi=150, bbox_inches='tight')
    plt.close(fig2)
    print("✅ Emotional distribution chart created")

    fig3 = visualizer.plot_care_exchange_heatmap(
        care_matrix, ['Guardian1', 'Guardian2', 'Guardian3'],
        ['SeedlingA', 'SeedlingB']
    )
    fig3.savefig('care_heatmap.png', dpi=150, bbox_inches='tight')
    plt.close(fig3)
    print("✅ Care exchange heatmap created")

    fig4 = visualizer.plot_shelter_climate_timeline(climate_history)
    fig4.savefig('climate_timeline.png', dpi=150, bbox_inches='tight')
    plt.close(fig4)
    print("✅ Climate timeline created")

    # Create comprehensive report
    visualizer.create_comprehensive_report(
        trust_history, emotional_states, care_matrix, climate_history,
        ['Guardian1', 'Guardian2', 'Guardian3'], ['SeedlingA', 'SeedlingB']
    )

    print("🎉 All visualizations completed!")


if __name__ == "__main__":
    demo_visualizations()
