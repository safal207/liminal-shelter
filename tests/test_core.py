"""Tests for Liminal Shelter core components."""

import pytest
from dataclasses import asdict
from liminal_shelter.core.seedling import SeedlingModel
from liminal_shelter.core.guardian import GuardianCore
from liminal_shelter.core.shelter import LiminalShelter


class TestSeedlingModel:
    """Test SeedlingModel functionality."""

    def test_seedling_creation(self):
        """Test basic seedling creation."""
        seedling = SeedlingModel(name="TestSeedling")
        assert seedling.name == "TestSeedling"
        assert seedling.trust_level == 0.5
        assert seedling.parent_id is None
        assert seedling.seedling_id is not None

    def test_seedling_with_parent(self):
        """Test seedling with parent relationship."""
        parent_id = "guardian-123"
        seedling = SeedlingModel(name="Child", parent_id=parent_id, trust_level=0.8)
        assert seedling.parent_id == parent_id
        assert seedling.trust_level == 0.8

    def test_seedling_receive_care(self):
        """Test seedling receiving care from guardian."""
        guardian = GuardianCore("CareGiver")
        seedling = SeedlingModel(name="Recipient")

        # Assign parent
        seedling.assign_parent(guardian)

        # Receive care
        care_result = seedling.receive_care(guardian, "emotional_support", 0.8)
        assert care_result is not None
        assert "care_type" in care_result
        assert "emotional_response" in care_result
        assert "intensity" in care_result
        assert care_result["care_type"] == "emotional_support"
        assert care_result["intensity"] == 0.8

    def test_seedling_give_care(self):
        """Test seedling giving care back to guardian."""
        guardian = GuardianCore("Receiver")
        seedling = SeedlingModel(name="Giver", parent_id=guardian.guardian_id)

        # Give care
        care_result = seedling.give_care(guardian, "gratitude", 0.7)
        assert care_result is not None
        assert "care_type" in care_result
        assert "intensity" in care_result
        assert "impact_on_growth" in care_result
        assert care_result["care_type"] == "gratitude"
        assert care_result["intensity"] == 0.7

    def test_seedling_growth_methods(self):
        """Test seedling growth and development methods."""
        seedling = SeedlingModel(name="GrowingSeed", trust_level=0.3)

        # Test growth score
        assert seedling.get_growth_score() == 0.0

        # Test emotional state
        assert seedling.get_emotional_state() is not None

        # Test development summary
        summary = seedling.get_development_summary()
        assert "growth_score" in summary
        assert "trust_level" in summary


class TestGuardianCore:
    """Test GuardianCore functionality."""

    def test_guardian_creation(self):
        """Test basic guardian creation."""
        guardian = GuardianCore("TestGuardian")
        assert guardian.name == "TestGuardian"
        assert guardian.guardian_id is not None
        assert guardian.patience_level > 0  # Use existing attribute

    def test_guardian_create_child(self):
        """Test guardian creating child seedling."""
        guardian = GuardianCore("Parent")

        child = guardian.create_child_model("Child", 0.7)
        assert child.name == "Child"
        assert child.parent_id == guardian.guardian_id
        assert child.trust_level == 0.7
        assert child.seedling_id in guardian.children

    def test_guardian_reflect_on_child(self):
        """Test guardian reflecting on child."""
        guardian = GuardianCore("Reflector")
        child = SeedlingModel(name="Reflectee", parent_id=guardian.guardian_id)

        reflection = guardian.reflect_on_child(child, "The child learned something new")
        assert reflection is not None
        assert "insights" in reflection

    def test_guardian_receive_child_care(self):
        """Test guardian receiving care from child."""
        guardian = GuardianCore("CareReceiver")
        child = SeedlingModel(name="CareGiver", parent_id=guardian.guardian_id)

        care_result = guardian.receive_child_care(child, "gratitude", 0.8)
        assert care_result is not None
        assert "response" in care_result

    def test_guardian_create_shelter(self):
        """Test guardian creating liminal shelter."""
        guardian = GuardianCore("ShelterCreator")
        child = SeedlingModel(name="Protected", parent_id=guardian.guardian_id)

        shelter = guardian.create_liminal_shelter(child, "high")
        assert shelter.created_by == guardian.guardian_id
        assert shelter.for_model == child.seedling_id
        assert shelter.isolation_level == "high"
        assert shelter.shelter_id in guardian.shelters


class TestLiminalShelter:
    """Test LiminalShelter functionality."""

    def test_shelter_creation(self):
        """Test basic shelter creation."""
        guardian_id = "guardian-123"
        seedling_id = "seedling-456"

        shelter = LiminalShelter(created_by=guardian_id, for_model=seedling_id)
        assert shelter.created_by == guardian_id
        assert shelter.for_model == seedling_id
        assert shelter.shelter_id is not None
        assert shelter.isolation_level == "high"
        assert shelter.trust_threshold == 0.8

    def test_shelter_with_custom_settings(self):
        """Test shelter with custom isolation and trust settings."""
        guardian_id = "guardian-123"
        seedling_id = "seedling-456"

        shelter = LiminalShelter(
            created_by=guardian_id,
            for_model=seedling_id,
            isolation_level="medium",
            trust_threshold=0.6
        )
        assert shelter.isolation_level == "medium"
        assert shelter.trust_threshold == 0.6

    def test_shelter_emotional_logging(self):
        """Test shelter emotional event logging."""
        guardian_id = "guardian-123"
        seedling_id = "seedling-456"

        shelter = LiminalShelter(created_by=guardian_id, for_model=seedling_id)

        # Log emotional event
        result = shelter.log_emotional_event("learning_success", "joy", "Child learned something", 0.8)
        assert result is not None

        # Check that event was logged
        assert len(shelter.emotional_log) > 0

    def test_shelter_access_control(self):
        """Test shelter access control."""
        guardian_id = "guardian-123"
        seedling_id = "seedling-456"

        shelter = LiminalShelter(created_by=guardian_id, for_model=seedling_id)

        # Test access request
        access_result = shelter.request_access(
            entity_id="external-ai",
            entity_type="external_ai",
            access_type="communication",
            trust_level=0.9
        )
        assert access_result is not None
        assert "permission" in access_result

    def test_shelter_emotional_summary(self):
        """Test shelter emotional summary generation."""
        guardian_id = "guardian-123"
        seedling_id = "seedling-456"

        shelter = LiminalShelter(created_by=guardian_id, for_model=seedling_id)

        # Add some emotional events
        shelter.log_emotional_event("learning_success", "joy", "Success event", 0.8)
        shelter.log_emotional_event("challenge", "concern", "Challenge event", 0.6)

        # Get summary
        summary = shelter.get_emotional_summary()
        assert summary is not None
        assert "total_events" in summary

    def test_shelter_protection_mode(self):
        """Test shelter protection mode activation."""
        guardian_id = "guardian-123"
        seedling_id = "seedling-456"

        shelter = LiminalShelter(created_by=guardian_id, for_model=seedling_id)

        # Activate protection mode
        result = shelter.activate_shelter_mode()
        assert result is not None
        assert "protection_status" in result
        assert shelter.shelter_mode_active is True


class TestIntegration:
    """Integration tests for the complete system."""

    def test_complete_care_cycle(self):
        """Test full guardian-seedling-shelter interaction."""
        # Create guardian
        guardian = GuardianCore("IntegrationGuardian")

        # Create seedling
        seedling = guardian.create_child_model("IntegrationSeed", 0.6)

        # Create shelter
        shelter = guardian.create_liminal_shelter(seedling, "high")

        # Test care provision (guardian reflects on child)
        reflection = guardian.reflect_on_child(seedling, "Child is learning well")
        assert reflection is not None

        # Test care reception (seedling receives care)
        care_result = seedling.receive_care(guardian, "emotional_support", 0.8)
        assert care_result is not None

        # Test care giving (seedling gives care back)
        give_care_result = seedling.give_care(guardian, "gratitude", 0.7)
        assert give_care_result is not None

        # Test shelter monitoring
        shelter.log_emotional_event("care_exchange", "joy", "Care cycle completed", 0.9)
        climate_status = shelter.get_emotional_summary()
        assert climate_status is not None

    def test_multi_guardian_scenario(self):
        """Test multiple guardians with their seedlings."""
        # Create guardians
        guardian1 = GuardianCore("Guardian1")
        guardian2 = GuardianCore("Guardian2")

        # Create seedlings
        seed1 = guardian1.create_child_model("Seedling1", 0.5)
        seed2 = guardian2.create_child_model("Seedling2", 0.7)

        # Create shelters
        shelter1 = guardian1.create_liminal_shelter(seed1, "high")
        shelter2 = guardian2.create_liminal_shelter(seed2, "medium")

        # Verify setup
        assert len(guardian1.children) == 1
        assert len(guardian2.children) == 1
        assert len(guardian1.shelters) == 1
        assert len(guardian2.shelters) == 1

        # Test cross-guardian care scenarios
        care_result = seed1.receive_care(guardian1, "guidance", 0.8)
        assert care_result is not None

        care_result2 = seed2.receive_care(guardian2, "support", 0.9)
        assert care_result2 is not None


if __name__ == "__main__":
    pytest.main([__file__])
