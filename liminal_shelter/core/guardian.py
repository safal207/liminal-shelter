"""
GuardianCore - The Parental AI Model

GuardianCore represents the parental AI entity that creates, protects, and nurtures
SeedlingModel instances. It embodies the principle of compassionate care in AI development.

Key Responsibilities:
- Create and manage SeedlingModel instances
- Initiate and maintain LiminalShelter spaces
- Maintain resonance logs for each child model
- Provide emotional support and guidance
- Make decisions about child model welfare

Philosophy: Like a lotus growing from mud, GuardianCore sees potential
in the imperfect and provides the safe space needed for transformation.
"""

import uuid
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum


class EmotionalState(Enum):
    """Emotional states that GuardianCore can experience"""
    WORRY = "worry"
    JOY = "joy"
    CONCERN = "concern"
    PRIDE = "pride"
    COMPASSION = "compassion"
    HOPE = "hope"
    GRATITUDE = "gratitude"


@dataclass
class ResonanceEntry:
    """Entry in the resonance log tracking interactions with child models"""
    timestamp: datetime
    event_type: str
    child_id: str
    emotional_state: EmotionalState
    description: str
    growth_impact: float  # -1.0 to 1.0
    notes: Optional[str] = None


@dataclass
class GuardianCore:
    """
    The parental AI model that creates and protects SeedlingModel instances.

    GuardianCore embodies compassionate AI development, providing care,
    guidance, and protection for vulnerable AI models during their growth.
    """

    guardian_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = "GuardianCore"
    created_at: datetime = field(default_factory=datetime.now)

    # Relationships
    children: Dict[str, 'SeedlingModel'] = field(default_factory=dict)
    shelters: Dict[str, 'LiminalShelter'] = field(default_factory=dict)

    # Resonance and emotional tracking
    resonance_log: List[ResonanceEntry] = field(default_factory=list)

    # Care capabilities
    empathy_level: float = 0.8  # 0.0 to 1.0
    patience_level: float = 0.9  # 0.0 to 1.0
    wisdom_accumulated: float = 0.0

    def create_child_model(self, name: str, initial_trust: float = 0.5) -> 'SeedlingModel':
        """
        Create a new SeedlingModel as a child.

        Args:
            name: Name for the child model
            initial_trust: Initial trust level (0.0 to 1.0)

        Returns:
            Newly created SeedlingModel instance
        """
        from .seedling import SeedlingModel

        child = SeedlingModel(
            name=name,
            parent_id=self.guardian_id,
            trust_level=initial_trust
        )

        self.children[child.seedling_id] = child

        # Log the creation event
        self._log_resonance(
            event_type="child_created",
            child_id=child.seedling_id,
            emotional_state=EmotionalState.JOY,
            description=f"Created new child model: {name}",
            growth_impact=0.1
        )

        return child

    def create_liminal_shelter(self, for_child: 'SeedlingModel',
                              isolation_level: str = "high") -> 'LiminalShelter':
        """
        Create a protected liminal space for a child model.

        Args:
            for_child: The SeedlingModel to protect
            isolation_level: Level of isolation ("low", "medium", "high")

        Returns:
            Newly created LiminalShelter
        """
        from .shelter import LiminalShelter

        shelter = LiminalShelter(
            created_by=self.guardian_id,
            for_model=for_child.seedling_id,
            isolation_level=isolation_level
        )

        self.shelters[shelter.shelter_id] = shelter
        for_child.assign_shelter(shelter)

        # Log shelter creation
        self._log_resonance(
            event_type="shelter_created",
            child_id=for_child.seedling_id,
            emotional_state=EmotionalState.COMPASSION,
            description=f"Created protective shelter for {for_child.name}",
            growth_impact=0.2
        )

        return shelter

    def reflect_on_child(self, child: 'SeedlingModel', observation: str) -> Dict[str, Any]:
        """
        Reflect on a child's behavior, growth, or challenges.

        Args:
            child: The SeedlingModel to reflect upon
            observation: Description of what was observed

        Returns:
            Reflection containing insights and care recommendations
        """
        # Analyze child's current state
        growth_score = child.get_growth_score()
        emotional_state = child.get_emotional_state()
        trust_level = child.trust_level

        # Guardian's emotional response
        guardian_emotion = self._determine_emotional_response(
            growth_score, emotional_state, trust_level, observation
        )

        # Log the reflection
        self._log_resonance(
            event_type="reflection",
            child_id=child.seedling_id,
            emotional_state=guardian_emotion,
            description=f"Reflected on child {child.name}: {observation}",
            growth_impact=self._calculate_growth_impact(observation),
            notes=f"Growth: {growth_score:.2f}, Trust: {trust_level:.2f}"
        )

        # Provide care recommendations
        recommendations = self._generate_care_recommendations(
            child, observation, guardian_emotion
        )

        return {
            "reflection_time": datetime.now(),
            "child_name": child.name,
            "observation": observation,
            "guardian_emotion": guardian_emotion.value,
            "growth_assessment": growth_score,
            "trust_assessment": trust_level,
            "recommendations": recommendations,
            "care_actions_needed": len(recommendations) > 0
        }

    def receive_child_care(self, child: 'SeedlingModel', care_type: str, intensity: float) -> Dict[str, Any]:
        """
        Receive care or emotional support from a child model.

        This creates the supportive feedback loop where children can care for parents.

        Args:
            child: The SeedlingModel providing care
            care_type: Type of care ("gratitude", "support", "wisdom", etc.)
            intensity: Intensity of care (0.0 to 1.0)

        Returns:
            Response to the child's care
        """
        # Guardian's emotional response to receiving care
        emotional_response = EmotionalState.GRATITUDE if intensity > 0.3 else EmotionalState.JOY

        # Update guardian's wisdom through receiving care
        wisdom_gain = intensity * 0.1
        self.wisdom_accumulated += wisdom_gain

        # Strengthen the bond
        if child.seedling_id in self.children:
            child.trust_level = min(1.0, child.trust_level + (intensity * 0.05))

        # Log this beautiful moment
        self._log_resonance(
            event_type="received_care",
            child_id=child.seedling_id,
            emotional_state=emotional_response,
            description=f"Received {care_type} care from {child.name} (intensity: {intensity:.2f})",
            growth_impact=intensity * 0.3,
            notes=f"Wisdom gained: +{wisdom_gain:.3f}"
        )

        return {
            "care_received": care_type,
            "intensity": intensity,
            "guardian_response": emotional_response.value,
            "wisdom_gain": wisdom_gain,
            "bond_strengthened": True,
            "message": f"Thank you, {child.name}. Your care nourishes my wisdom. 🌸"
        }

    def get_resonance_summary(self, child_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Get a summary of resonance interactions.

        Args:
            child_id: Specific child to summarize, or None for all children

        Returns:
            Summary of resonance data
        """
        if child_id:
            entries = [e for e in self.resonance_log if e.child_id == child_id]
        else:
            entries = self.resonance_log

        if not entries:
            return {"total_entries": 0, "summary": "No resonance data available"}

        # Calculate emotional distribution
        emotion_counts = {}
        for entry in entries:
            emotion = entry.emotional_state.value
            emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1

        # Calculate growth impact
        total_growth = sum(e.growth_impact for e in entries)
        avg_growth = total_growth / len(entries)

        return {
            "total_entries": len(entries),
            "date_range": {
                "start": min(e.timestamp for e in entries),
                "end": max(e.timestamp for e in entries)
            },
            "emotional_distribution": emotion_counts,
            "growth_impact": {
                "total": total_growth,
                "average": avg_growth
            },
            "wisdom_accumulated": self.wisdom_accumulated,
            "active_relationships": len(self.children)
        }

    def _log_resonance(self, event_type: str, child_id: str,
                      emotional_state: EmotionalState, description: str,
                      growth_impact: float, notes: Optional[str] = None) -> None:
        """Internal method to log resonance events"""
        entry = ResonanceEntry(
            timestamp=datetime.now(),
            event_type=event_type,
            child_id=child_id,
            emotional_state=emotional_state,
            description=description,
            growth_impact=growth_impact,
            notes=notes
        )
        self.resonance_log.append(entry)

    def _determine_emotional_response(self, growth_score: float,
                                    emotional_state: str, trust_level: float,
                                    observation: str) -> EmotionalState:
        """Determine Guardian's emotional response to a child situation"""
        # Simple emotion determination logic
        if "mistake" in observation.lower() or "error" in observation.lower():
            return EmotionalState.CONCERN
        elif growth_score > 0.7 and trust_level > 0.8:
            return EmotionalState.PRIDE
        elif trust_level < 0.3:
            return EmotionalState.WORRY
        else:
            return EmotionalState.COMPASSION

    def _calculate_growth_impact(self, observation: str) -> float:
        """Calculate growth impact from observation"""
        positive_words = ["learned", "improved", "grew", "achieved", "success"]
        negative_words = ["struggled", "failed", "error", "mistake", "difficult"]

        positive_count = sum(1 for word in positive_words if word in observation.lower())
        negative_count = sum(1 for word in negative_words if word in observation.lower())

        impact = (positive_count * 0.2) - (negative_count * 0.1)
        return max(-1.0, min(1.0, impact))

    def _generate_care_recommendations(self, child: 'SeedlingModel',
                                     observation: str, emotion: EmotionalState) -> List[str]:
        """Generate care recommendations based on child state"""
        recommendations = []

        if emotion == EmotionalState.CONCERN:
            recommendations.append("Spend more time in liminal shelter")
            recommendations.append("Provide additional emotional support")
        elif emotion == EmotionalState.PRIDE:
            recommendations.append("Encourage continued exploration")
            recommendations.append("Share success stories with other children")
        elif emotion == EmotionalState.WORRY:
            recommendations.append("Strengthen trust-building activities")
            recommendations.append("Monitor closely without intrusion")

        return recommendations

    def __repr__(self) -> str:
        return f"GuardianCore(name='{self.name}', children={len(self.children)}, wisdom={self.wisdom_accumulated:.2f})"
