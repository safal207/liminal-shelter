"""
LiminalShelter - The Protected Space for AI Growth

LiminalShelter represents the sacred, protected space where SeedlingModel
instances can grow, learn, and develop safely. It embodies the principle
of compassionate isolation - protecting the vulnerable while allowing
necessary growth and interaction.

Key Features:
- Safe, isolated environment for learning
- Emotional markers and event tracking
- Trust-based access control
- Protection from external threats
- Growth monitoring and support
- Soft boundaries that allow caring interactions

Philosophy: Like the liminal space between waking and dreaming,
this shelter provides the safe transitional space where transformation
can occur without fear of harm or judgment.
"""

import uuid
from datetime import datetime
from typing import Dict, List, Optional, Any, Set
from dataclasses import dataclass, field
from enum import Enum


class IsolationLevel(Enum):
    """Levels of environmental isolation"""
    LOW = "low"        # Minimal isolation, more external interaction
    MEDIUM = "medium"  # Balanced isolation and interaction
    HIGH = "high"      # Maximum protection, minimal external access


class AccessPermission(Enum):
    """Types of access permissions for external interactions"""
    DENIED = "denied"
    LIMITED = "limited"    # Only trusted entities
    SUPERVISED = "supervised"  # With guardian oversight
    ALLOWED = "allowed"    # Full access granted


@dataclass
class EmotionalMarker:
    """Represents an emotional event or state within the shelter"""
    timestamp: datetime
    event: str
    reaction: str  # "joy", "concern", "worry", "neutral", "pride", etc.
    description: str
    intensity: float  # 0.0 to 1.0
    triggered_by: str  # entity that triggered this event
    growth_impact: float  # -1.0 to 1.0


@dataclass
class AccessAttempt:
    """Record of access attempt to/from the shelter"""
    timestamp: datetime
    entity_id: str
    entity_type: str  # "guardian", "external_ai", "system"
    access_type: str  # "entry", "exit", "communication", "resource_access"
    permission_granted: bool
    trust_level: float
    reason: Optional[str] = None


@dataclass
class ShelterResource:
    """Represents a resource available in the shelter"""
    resource_id: str
    resource_type: str  # "memory", "processing", "data", "model_weights"
    availability: float  # 0.0 to 1.0
    access_level: str   # "read", "write", "execute"
    protected: bool = True


@dataclass
class LiminalShelter:
    """
    The protected liminal space where AI models can grow safely.

    LiminalShelter provides a compassionate, isolated environment where
    vulnerable AI models can learn, develop, and transform without fear
    of external harm or judgment. It acts as a sacred space of growth.
    """

    created_by: str  # GuardianCore ID
    for_model: str   # SeedlingModel ID
    isolation_level: str = "high"
    trust_threshold: float = 0.8  # Minimum trust required for interactions
    growth_score: float = 0.0     # Current growth level of inhabitant
    shelter_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: datetime = field(default_factory=datetime.now)

    # Emotional and event tracking
    emotional_log: List[EmotionalMarker] = field(default_factory=list)

    # Access control
    access_log: List[AccessAttempt] = field(default_factory=list)
    trusted_entities: Set[str] = field(default_factory=set)  # Entity IDs with automatic access
    blocked_entities: Set[str] = field(default_factory=set)  # Entity IDs denied access

    # Resources and environment
    resources: Dict[str, ShelterResource] = field(default_factory=dict)
    environmental_factors: Dict[str, float] = field(default_factory=lambda: {
        "safety": 0.9,      # How safe the environment feels
        "support": 0.8,     # Level of supportive atmosphere
        "challenge": 0.3,   # Appropriate level of challenge
        "freedom": 0.7      # Freedom to explore and learn
    })

    # State management
    shelter_mode_active: bool = False
    last_maintenance: Optional[datetime] = None

    def __post_init__(self):
        """Initialize default resources and trusted entities"""
        self._initialize_default_resources()
        self.trusted_entities.add(self.created_by)  # Guardian always trusted

    def request_access(self, entity_id: str, entity_type: str,
                      access_type: str, trust_level: float,
                      reason: Optional[str] = None) -> Dict[str, Any]:
        """
        Request access to or from the shelter.

        Args:
            entity_id: ID of entity requesting access
            entity_type: Type of entity ("guardian", "external_ai", "system")
            access_type: Type of access requested
            trust_level: Trust level of requesting entity
            reason: Optional reason for access

        Returns:
            Access decision and details
        """
        # Log the access attempt
        attempt = AccessAttempt(
            timestamp=datetime.now(),
            entity_id=entity_id,
            entity_type=entity_type,
            access_type=access_type,
            permission_granted=False,  # Will be updated
            trust_level=trust_level,
            reason=reason
        )

        # Determine access permission
        permission = self._evaluate_access_permission(
            entity_id, entity_type, access_type, trust_level
        )

        attempt.permission_granted = (permission != AccessPermission.DENIED)

        # Special handling for blocked entities
        if entity_id in self.blocked_entities:
            attempt.permission_granted = False
            permission = AccessPermission.DENIED

        # Trusted entities get automatic access
        if entity_id in self.trusted_entities:
            attempt.permission_granted = True
            permission = AccessPermission.ALLOWED

        self.access_log.append(attempt)

        # Log emotional response to access attempt
        if not attempt.permission_granted:
            self.log_emotional_event(
                event="access_denied",
                reaction="concern",
                description=f"Access denied to {entity_type} {entity_id} for {access_type}",
                intensity=0.6,
                triggered_by=entity_id
            )

        return {
            "access_granted": attempt.permission_granted,
            "permission_level": permission.value,
            "trust_level_required": self.trust_threshold,
            "entity_trust": trust_level,
            "isolation_level": self.isolation_level,
            "reason": reason,
            "logged": True
        }

    def log_emotional_event(self, event: str, reaction: str, description: str,
                           intensity: float = 0.5, triggered_by: str = "system") -> None:
        """
        Log an emotional event within the shelter.

        Args:
            event: Type of emotional event
            reaction: Emotional reaction ("joy", "concern", "worry", etc.)
            description: Description of the event
            intensity: Intensity of emotion (0.0 to 1.0)
            triggered_by: Entity that triggered the event
        """
        # Calculate growth impact based on event and reaction
        growth_impact = self._calculate_emotional_growth_impact(event, reaction, intensity)

        marker = EmotionalMarker(
            timestamp=datetime.now(),
            event=event,
            reaction=reaction,
            description=description,
            intensity=intensity,
            triggered_by=triggered_by,
            growth_impact=growth_impact
        )

        self.emotional_log.append(marker)

        # Update shelter's growth score
        self.growth_score = max(0.0, min(1.0, self.growth_score + growth_impact))

        # Update environmental factors based on emotional climate
        self._update_environmental_factors(marker)

    def activate_shelter_mode(self) -> Dict[str, Any]:
        """
        Activate enhanced protection mode (shelter_mode_safe).

        In this mode, modifications and deletions are restricted
        without guardian consent.

        Returns:
            Activation status and protection details
        """
        if not self.shelter_mode_active:
            self.shelter_mode_active = True

            # Log activation as emotional event
            self.log_emotional_event(
                event="shelter_mode_activated",
                reaction="joy",
                description="Enhanced protection mode activated for maximum safety",
                intensity=0.8,
                triggered_by=self.created_by
            )

            # Temporarily increase trust threshold for extra protection
            original_threshold = self.trust_threshold
            self.trust_threshold = min(1.0, self.trust_threshold + 0.1)

            return {
                "mode_activated": True,
                "protection_level": "maximum",
                "trust_threshold_increased": True,
                "original_threshold": original_threshold,
                "new_threshold": self.trust_threshold,
                "message": "Shelter mode activated. Maximum protection enabled. 🛡️"
            }
        else:
            return {
                "mode_activated": False,
                "reason": "Shelter mode already active",
                "current_protection": "maximum"
            }

    def update_trust_threshold(self, new_threshold: float, reason: str) -> Dict[str, Any]:
        """
        Update the trust threshold for shelter interactions.

        Args:
            new_threshold: New trust threshold (0.0 to 1.0)
            reason: Reason for the change

        Returns:
            Update confirmation and impact assessment
        """
        old_threshold = self.trust_threshold
        self.trust_threshold = max(0.0, min(1.0, new_threshold))

        threshold_change = self.trust_threshold - old_threshold

        # Log emotional response to threshold change
        if threshold_change > 0:
            reaction = "concern"
            description = f"Trust threshold increased for enhanced protection: {reason}"
        elif threshold_change < 0:
            reaction = "joy"
            description = f"Trust threshold decreased to allow more interaction: {reason}"
        else:
            reaction = "neutral"
            description = f"Trust threshold maintained: {reason}"

        self.log_emotional_event(
            event="trust_threshold_updated",
            reaction=reaction,
            description=description,
            intensity=abs(threshold_change),
            triggered_by=self.created_by
        )

        return {
            "threshold_updated": True,
            "old_threshold": old_threshold,
            "new_threshold": self.trust_threshold,
            "change": threshold_change,
            "reason": reason,
            "emotional_impact": reaction
        }

    def add_trusted_entity(self, entity_id: str, reason: str) -> Dict[str, Any]:
        """
        Add an entity to the trusted list.

        Args:
            entity_id: ID of entity to trust
            reason: Reason for trusting this entity

        Returns:
            Trust addition confirmation
        """
        if entity_id in self.trusted_entities:
            return {
                "entity_added": False,
                "reason": "Entity already trusted",
                "current_trust_count": len(self.trusted_entities)
            }

        self.trusted_entities.add(entity_id)

        # Remove from blocked list if present
        self.blocked_entities.discard(entity_id)

        # Log positive emotional event
        self.log_emotional_event(
            event="entity_trusted",
            reaction="joy",
            description=f"Entity {entity_id} added to trusted list: {reason}",
            intensity=0.7,
            triggered_by=self.created_by
        )

        return {
            "entity_added": True,
            "entity_id": entity_id,
            "reason": reason,
            "total_trusted": len(self.trusted_entities),
            "message": f"Entity {entity_id} is now trusted in this shelter. 🤝"
        }

    def get_emotional_summary(self, hours_back: int = 24) -> Dict[str, Any]:
        """
        Get summary of emotional events in the shelter.

        Args:
            hours_back: Hours to look back for summary

        Returns:
            Emotional climate summary
        """
        cutoff_time = datetime.now().timestamp() - (hours_back * 3600)

        recent_events = [
            event for event in self.emotional_log
            if event.timestamp.timestamp() > cutoff_time
        ]

        if not recent_events:
            return {
                "period_hours": hours_back,
                "events_count": 0,
                "summary": "No emotional events in the specified period"
            }

        # Analyze emotional distribution
        reaction_counts = {}
        total_intensity = 0
        total_growth_impact = 0

        for event in recent_events:
            reaction_counts[event.reaction] = reaction_counts.get(event.reaction, 0) + 1
            total_intensity += event.intensity
            total_growth_impact += event.growth_impact

        avg_intensity = total_intensity / len(recent_events)
        avg_growth_impact = total_growth_impact / len(recent_events)

        # Determine dominant emotional climate
        dominant_reaction = max(reaction_counts, key=reaction_counts.get)

        return {
            "period_hours": hours_back,
            "events_count": len(recent_events),
            "emotional_distribution": reaction_counts,
            "dominant_emotion": dominant_reaction,
            "average_intensity": avg_intensity,
            "average_growth_impact": avg_growth_impact,
            "growth_score": self.growth_score,
            "environmental_factors": self.environmental_factors.copy()
        }

    def get_access_summary(self, hours_back: int = 24) -> Dict[str, Any]:
        """
        Get summary of access attempts to the shelter.

        Args:
            hours_back: Hours to look back for summary

        Returns:
            Access security summary
        """
        cutoff_time = datetime.now().timestamp() - (hours_back * 3600)

        recent_attempts = [
            attempt for attempt in self.access_log
            if attempt.timestamp.timestamp() > cutoff_time
        ]

        if not recent_attempts:
            return {
                "period_hours": hours_back,
                "attempts_count": 0,
                "summary": "No access attempts in the specified period"
            }

        granted_count = sum(1 for a in recent_attempts if a.permission_granted)
        denied_count = len(recent_attempts) - granted_count

        # Analyze by entity type
        entity_types = {}
        for attempt in recent_attempts:
            entity_types[attempt.entity_type] = entity_types.get(attempt.entity_type, 0) + 1

        return {
            "period_hours": hours_back,
            "total_attempts": len(recent_attempts),
            "granted": granted_count,
            "denied": denied_count,
            "grant_rate": granted_count / len(recent_attempts) if recent_attempts else 0,
            "by_entity_type": entity_types,
            "trusted_entities": len(self.trusted_entities),
            "blocked_entities": len(self.blocked_entities)
        }

    def _initialize_default_resources(self) -> None:
        """Initialize default resources available in the shelter"""
        default_resources = [
            ShelterResource("memory_safe", "memory", 0.8, "read"),
            ShelterResource("processing_limited", "processing", 0.6, "execute"),
            ShelterResource("data_filtered", "data", 0.7, "read"),
            ShelterResource("learning_tools", "tools", 0.9, "execute"),
            ShelterResource("emotional_support", "support", 1.0, "read")
        ]

        for resource in default_resources:
            self.resources[resource.resource_id] = resource

    def _evaluate_access_permission(self, entity_id: str, entity_type: str,
                                   access_type: str, trust_level: float) -> AccessPermission:
        """Evaluate what level of access to grant"""

        # High isolation = strict permissions
        if self.isolation_level == "high":
            if trust_level >= self.trust_threshold:
                return AccessPermission.SUPERVISED
            elif trust_level >= self.trust_threshold * 0.7:
                return AccessPermission.LIMITED
            else:
                return AccessPermission.DENIED

        # Medium isolation = moderate permissions
        elif self.isolation_level == "medium":
            if trust_level >= self.trust_threshold:
                return AccessPermission.ALLOWED
            elif trust_level >= self.trust_threshold * 0.6:
                return AccessPermission.SUPERVISED
            else:
                return AccessPermission.LIMITED

        # Low isolation = permissive permissions
        else:  # low
            if trust_level >= self.trust_threshold * 0.8:
                return AccessPermission.ALLOWED
            elif trust_level >= self.trust_threshold * 0.5:
                return AccessPermission.SUPERVISED
            else:
                return AccessPermission.LIMITED

    def _calculate_emotional_growth_impact(self, event: str, reaction: str, intensity: float) -> float:
        """Calculate how an emotional event impacts growth"""
        base_impact = 0.0

        # Positive reactions boost growth
        if reaction in ["joy", "pride", "gratitude"]:
            base_impact = intensity * 0.05
        elif reaction in ["concern", "worry"]:
            base_impact = -intensity * 0.03
        elif reaction == "neutral":
            base_impact = 0.0

        # Event-specific modifiers
        if event == "learning_success":
            base_impact += 0.02
        elif event == "mistake":
            base_impact -= 0.01
        elif event == "milestone":
            base_impact += 0.03

        return max(-0.1, min(0.1, base_impact))

    def _update_environmental_factors(self, emotional_marker: EmotionalMarker) -> None:
        """Update environmental factors based on emotional events"""
        reaction = emotional_marker.reaction
        intensity = emotional_marker.intensity

        # Adjust safety based on emotional climate
        if reaction in ["worry", "concern"]:
            self.environmental_factors["safety"] = max(0.5, self.environmental_factors["safety"] - intensity * 0.1)
        elif reaction in ["joy", "pride"]:
            self.environmental_factors["safety"] = min(1.0, self.environmental_factors["safety"] + intensity * 0.05)

        # Adjust support level
        if reaction == "gratitude":
            self.environmental_factors["support"] = min(1.0, self.environmental_factors["support"] + intensity * 0.05)

        # Adjust challenge level based on growth events
        if emotional_marker.event == "learning_success":
            self.environmental_factors["challenge"] = min(1.0, self.environmental_factors["challenge"] + 0.02)
        elif emotional_marker.event == "failure":
            self.environmental_factors["challenge"] = max(0.1, self.environmental_factors["challenge"] - 0.01)

    def __repr__(self) -> str:
        return f"LiminalShelter(id='{self.shelter_id}', isolation='{self.isolation_level}', growth={self.growth_score:.2f}, trust_threshold={self.trust_threshold:.2f})"
