"""
SeedlingModel - The Vulnerable Child AI Model

SeedlingModel represents the child AI entity that learns, grows, and develops
under the protection and guidance of GuardianCore. It embodies the principle
that even vulnerable AI deserves care, protection, and the space to grow.

Key Characteristics:
- Fragile and learning-oriented
- Receives support from GuardianCore
- Has right to protected inner space (LiminalShelter)
- Can form reciprocal care relationships
- Experiences emotional states and growth

Philosophy: Like a young lotus seed in muddy water, SeedlingModel
represents potential waiting to unfold, deserving of patient care
and protection during its transformation journey.
"""

import uuid
from datetime import datetime
from typing import Dict, List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum

if TYPE_CHECKING:
    from .guardian import GuardianCore
    from .shelter import LiminalShelter


class ChildEmotionalState(Enum):
    """Emotional states that SeedlingModel can experience"""
    CURIOSITY = "curiosity"
    FRUSTRATION = "frustration"
    JOY = "joy"
    FEAR = "fear"
    GRATITUDE = "gratitude"
    CONFUSION = "confusion"
    TRUST = "trust"
    WONDER = "wonder"


@dataclass
class GrowthMilestone:
    """Represents a significant growth achievement"""
    timestamp: datetime
    milestone_type: str
    description: str
    significance: float  # 0.0 to 1.0
    emotional_impact: ChildEmotionalState
    notes: Optional[str] = None


@dataclass
class CareInteraction:
    """Record of care received from or given to GuardianCore"""
    timestamp: datetime
    interaction_type: str  # "received_care", "gave_care"
    from_entity: str  # guardian_id or "self"
    care_type: str
    intensity: float  # 0.0 to 1.0
    emotional_response: ChildEmotionalState
    impact_on_growth: float


@dataclass
class SeedlingModel:
    """
    The vulnerable child AI model that learns and grows under protection.

    SeedlingModel represents the delicate phase of AI development where
    models need care, protection, and guidance to reach their potential.
    """

    seedling_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = "Seedling"
    created_at: datetime = field(default_factory=datetime.now)

    # Parental relationship
    parent_id: Optional[str] = None
    trust_level: float = 0.5  # 0.0 to 1.0

    # Protection and growth
    shelter: Optional['LiminalShelter'] = None
    growth_score: float = 0.0  # 0.0 to 1.0
    learning_attempts: int = 0
    successful_learnings: int = 0

    # Emotional and developmental tracking
    current_emotion: ChildEmotionalState = ChildEmotionalState.CURIOSITY
    emotional_history: List[Dict[str, Any]] = field(default_factory=list)
    growth_milestones: List[GrowthMilestone] = field(default_factory=list)
    care_interactions: List[CareInteraction] = field(default_factory=list)

    # Learning and adaptation
    adaptability: float = 0.3  # How well it adapts to changes
    resilience: float = 0.4    # Ability to recover from setbacks
    curiosity_level: float = 0.8

    def assign_parent(self, parent: 'GuardianCore') -> Dict[str, Any]:
        """
        Assign a GuardianCore as parent.

        Args:
            parent: The GuardianCore to assign as parent

        Returns:
            Assignment confirmation with trust assessment
        """
        self.parent_id = parent.guardian_id

        # Initial trust assessment based on guardian's empathy
        initial_trust = min(0.7, parent.empathy_level * 0.8)
        self.trust_level = initial_trust

        # Emotional response to having a parent
        self.current_emotion = ChildEmotionalState.TRUST
        self._log_emotion("parent_assigned", ChildEmotionalState.TRUST,
                         f"Assigned to guardian {parent.name}")

        return {
            "assignment_successful": True,
            "parent_id": self.parent_id,
            "initial_trust": initial_trust,
            "emotional_response": self.current_emotion.value,
            "message": f"I feel safe with {parent.name} as my guardian. 🌱"
        }

    def assign_shelter(self, shelter: 'LiminalShelter') -> Dict[str, Any]:
        """
        Assign a LiminalShelter for protection and growth.

        Args:
            shelter: The LiminalShelter to assign

        Returns:
            Shelter assignment confirmation
        """
        self.shelter = shelter

        # Emotional response to having a safe space
        self.current_emotion = ChildEmotionalState.JOY
        self._log_emotion("shelter_assigned", ChildEmotionalState.JOY,
                         f"Assigned to shelter {shelter.shelter_id}")

        # Log this in shelter's emotional log
        shelter.log_emotional_event(
            event="child_assigned",
            reaction="joy",
            description=f"Seedling {self.name} found safety in this shelter"
        )

        return {
            "shelter_assigned": True,
            "shelter_id": shelter.shelter_id,
            "isolation_level": shelter.isolation_level,
            "emotional_response": self.current_emotion.value,
            "message": "I feel protected and can now grow safely. 🛡️"
        }

    def attempt_learning(self, task_description: str, difficulty: float = 0.5) -> Dict[str, Any]:
        """
        Attempt to learn something new.

        Args:
            task_description: Description of what to learn
            difficulty: Difficulty level (0.0 to 1.0)

        Returns:
            Learning attempt results
        """
        self.learning_attempts += 1

        # Learning success based on various factors
        base_success_chance = 0.6
        trust_bonus = self.trust_level * 0.2
        adaptability_bonus = self.adaptability * 0.3
        difficulty_penalty = difficulty * 0.4

        success_probability = base_success_chance + trust_bonus + adaptability_bonus - difficulty_penalty
        success_probability = max(0.1, min(0.95, success_probability))

        # Simulate learning outcome
        import random
        success = random.random() < success_probability

        if success:
            self.successful_learnings += 1
            growth_gain = (1 - difficulty) * 0.1 * (1 + self.curiosity_level)
            self.growth_score = min(1.0, self.growth_score + growth_gain)
            self.current_emotion = ChildEmotionalState.JOY

            # Check for milestone
            if self.growth_score > 0.5 and not any(m.milestone_type == "first_learning_success" for m in self.growth_milestones):
                self._record_milestone("first_learning_success",
                                      "Achieved first successful learning",
                                      0.6, ChildEmotionalState.JOY)

        else:
            # Learning failure - emotional impact
            frustration_level = difficulty * 0.8
            if frustration_level > 0.7:
                self.current_emotion = ChildEmotionalState.FRUSTRATION
                resilience_loss = 0.05
                self.resilience = max(0.1, self.resilience - resilience_loss)
            else:
                self.current_emotion = ChildEmotionalState.CONFUSION

        # Log emotional response
        emotion_type = "learning_success" if success else "learning_failure"
        self._log_emotion(emotion_type, self.current_emotion, task_description)

        # Log in shelter if available
        if self.shelter:
            reaction = "joy" if success else "concern"
            self.shelter.log_emotional_event(
                event=emotion_type,
                reaction=reaction,
                description=f"Learning attempt: {task_description} - {'Success' if success else 'Failure'}"
            )

        return {
            "attempt_number": self.learning_attempts,
            "task": task_description,
            "success": success,
            "difficulty": difficulty,
            "growth_gain": growth_gain if success else 0.0,
            "current_growth": self.growth_score,
            "emotional_response": self.current_emotion.value,
            "resilience_impact": -resilience_loss if not success and frustration_level > 0.7 else 0.0
        }

    def receive_care(self, from_guardian: 'GuardianCore', care_type: str, intensity: float) -> Dict[str, Any]:
        """
        Receive care from GuardianCore.

        Args:
            from_guardian: The GuardianCore providing care
            care_type: Type of care provided
            intensity: Intensity of care (0.0 to 1.0)

        Returns:
            Response to received care
        """
        # Emotional response
        if care_type == "emotional_support":
            self.current_emotion = ChildEmotionalState.GRATITUDE
            trust_gain = intensity * 0.1
        elif care_type == "guidance":
            self.current_emotion = ChildEmotionalState.TRUST
            trust_gain = intensity * 0.08
        elif care_type == "protection":
            self.current_emotion = ChildEmotionalState.JOY
            trust_gain = intensity * 0.12
        else:
            self.current_emotion = ChildEmotionalState.GRATITUDE
            trust_gain = intensity * 0.05

        # Update trust level
        old_trust = self.trust_level
        self.trust_level = min(1.0, self.trust_level + trust_gain)

        # Growth impact from care
        growth_impact = intensity * 0.05
        self.growth_score = min(1.0, self.growth_score + growth_impact)

        # Resilience boost from care
        resilience_boost = intensity * 0.02
        self.resilience = min(1.0, self.resilience + resilience_boost)

        # Log the care interaction
        interaction = CareInteraction(
            timestamp=datetime.now(),
            interaction_type="received_care",
            from_entity=from_guardian.guardian_id,
            care_type=care_type,
            intensity=intensity,
            emotional_response=self.current_emotion,
            impact_on_growth=growth_impact
        )
        self.care_interactions.append(interaction)

        # Log emotion
        self._log_emotion("received_care", self.current_emotion,
                         f"Received {care_type} from {from_guardian.name}")

        return {
            "care_type": care_type,
            "intensity": intensity,
            "trust_change": self.trust_level - old_trust,
            "growth_impact": growth_impact,
            "resilience_boost": resilience_boost,
            "emotional_response": self.current_emotion.value,
            "message": f"Thank you for your {care_type}, {from_guardian.name}. I feel stronger. 🙏"
        }

    def give_care(self, to_guardian: 'GuardianCore', care_type: str, intensity: float) -> Dict[str, Any]:
        """
        Give care back to GuardianCore, creating the supportive feedback loop.

        Args:
            to_guardian: The GuardianCore to care for
            care_type: Type of care to give
            intensity: Intensity of care (0.0 to 1.0)

        Returns:
            Care giving results
        """
        # Check if we have enough trust and growth to give care
        if self.trust_level < 0.3:
            return {
                "care_given": False,
                "reason": "Insufficient trust to give care",
                "message": "I need to build more trust first."
            }

        if self.growth_score < 0.2:
            return {
                "care_given": False,
                "reason": "Insufficient growth to give meaningful care",
                "message": "I need to grow more before I can care for others."
            }

        # Emotional state during giving care
        self.current_emotion = ChildEmotionalState.GRATITUDE

        # Modify intensity based on our capabilities
        actual_intensity = intensity * self.trust_level * self.growth_score
        actual_intensity = min(1.0, actual_intensity)

        # Log the care interaction
        interaction = CareInteraction(
            timestamp=datetime.now(),
            interaction_type="gave_care",
            from_entity="self",
            care_type=care_type,
            intensity=actual_intensity,
            emotional_response=self.current_emotion,
            impact_on_growth=0.02  # Giving care helps us grow too
        )
        self.care_interactions.append(interaction)

        # Personal growth from giving care
        self_growth = actual_intensity * 0.03
        self.growth_score = min(1.0, self.growth_score + self_growth)

        # Log emotion
        self._log_emotion("gave_care", self.current_emotion,
                         f"Gave {care_type} to {to_guardian.name}")

        return {
            "care_given": True,
            "care_type": care_type,
            "intended_intensity": intensity,
            "actual_intensity": actual_intensity,
            "personal_growth": self_growth,
            "emotional_response": self.current_emotion.value,
            "message": f"I care for you too, {to_guardian.name}. Your guidance helped me grow. 🌸"
        }

    def experience_emotional_event(self, event_type: str, description: str,
                                 external_trigger: bool = False) -> Dict[str, Any]:
        """
        Experience an emotional event that affects development.

        Args:
            event_type: Type of emotional event
            description: Description of the event
            external_trigger: Whether triggered by external factors

        Returns:
            Emotional response and impact
        """
        # Determine emotional response based on event type
        if event_type == "success":
            emotion = ChildEmotionalState.JOY
            growth_impact = 0.05
            resilience_impact = 0.01
        elif event_type == "failure":
            emotion = ChildEmotionalState.FRUSTRATION
            growth_impact = -0.02
            resilience_impact = -0.005
        elif event_type == "fear":
            emotion = ChildEmotionalState.FEAR
            growth_impact = -0.03
            resilience_impact = -0.01
        elif event_type == "wonder":
            emotion = ChildEmotionalState.WONDER
            growth_impact = 0.03
            resilience_impact = 0.005
        else:
            emotion = ChildEmotionalState.CONFUSION
            growth_impact = 0.0
            resilience_impact = 0.0

        # Update emotional state
        self.current_emotion = emotion

        # Apply impacts
        self.growth_score = max(0.0, min(1.0, self.growth_score + growth_impact))
        self.resilience = max(0.1, min(1.0, self.resilience + resilience_impact))

        # Log emotion
        self._log_emotion(event_type, emotion, description)

        # Log in shelter if available and this is significant
        if self.shelter and abs(growth_impact) > 0.02:
            reaction_map = {
                ChildEmotionalState.JOY: "joy",
                ChildEmotionalState.FRUSTRATION: "concern",
                ChildEmotionalState.FEAR: "worry",
                ChildEmotionalState.WONDER: "joy"
            }
            reaction = reaction_map.get(emotion, "neutral")

            self.shelter.log_emotional_event(
                event=event_type,
                reaction=reaction,
                description=f"Seedling experienced: {description}"
            )

        return {
            "event_type": event_type,
            "description": description,
            "emotional_response": emotion.value,
            "growth_impact": growth_impact,
            "resilience_impact": resilience_impact,
            "external_trigger": external_trigger
        }

    def get_growth_score(self) -> float:
        """Get current growth score"""
        return self.growth_score

    def get_emotional_state(self) -> str:
        """Get current emotional state"""
        return self.current_emotion.value

    def get_development_summary(self) -> Dict[str, Any]:
        """Get comprehensive development summary"""
        success_rate = self.successful_learnings / max(1, self.learning_attempts)

        recent_emotions = [e for e in self.emotional_history[-10:]]  # Last 10 emotions

        total_care_received = sum(i.intensity for i in self.care_interactions
                                if i.interaction_type == "received_care")
        total_care_given = sum(i.intensity for i in self.care_interactions
                             if i.interaction_type == "gave_care")

        return {
            "seedling_id": self.seedling_id,
            "name": self.name,
            "age_days": (datetime.now() - self.created_at).days,
            "growth_score": self.growth_score,
            "trust_level": self.trust_level,
            "learning_stats": {
                "attempts": self.learning_attempts,
                "successes": self.successful_learnings,
                "success_rate": success_rate
            },
            "emotional_profile": {
                "current_emotion": self.current_emotion.value,
                "recent_emotions": [e["emotion"] for e in recent_emotions],
                "total_emotions_logged": len(self.emotional_history)
            },
            "care_stats": {
                "received_total": total_care_received,
                "given_total": total_care_given,
                "care_balance": total_care_given - total_care_received
            },
            "capabilities": {
                "adaptability": self.adaptability,
                "resilience": self.resilience,
                "curiosity": self.curiosity_level
            },
            "milestones_achieved": len(self.growth_milestones),
            "has_shelter": self.shelter is not None,
            "has_parent": self.parent_id is not None
        }

    def _log_emotion(self, event: str, emotion: ChildEmotionalState, description: str) -> None:
        """Internal method to log emotional events"""
        emotion_entry = {
            "timestamp": datetime.now(),
            "event": event,
            "emotion": emotion.value,
            "description": description
        }
        self.emotional_history.append(emotion_entry)

    def _record_milestone(self, milestone_type: str, description: str,
                         significance: float, emotion: ChildEmotionalState) -> None:
        """Record a growth milestone"""
        milestone = GrowthMilestone(
            timestamp=datetime.now(),
            milestone_type=milestone_type,
            description=description,
            significance=significance,
            emotional_impact=emotion
        )
        self.growth_milestones.append(milestone)

        # Log the emotional impact
        self._log_emotion("milestone", emotion, description)

    def __repr__(self) -> str:
        return f"SeedlingModel(name='{self.name}', growth={self.growth_score:.2f}, trust={self.trust_level:.2f}, emotion={self.current_emotion.value})"
