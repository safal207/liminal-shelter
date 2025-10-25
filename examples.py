"""Additional usage examples for Liminal Shelter."""

from liminal_shelter.core.seedling import SeedlingModel
from liminal_shelter.core.guardian import GuardianCore
from liminal_shelter.core.shelter import LiminalShelter
import time


def example_basic_care():
    """Basic care relationship example."""
    print("🌱 Example 1: Basic Care Relationship")
    print("=" * 40)

    # Create guardian and seedling
    guardian = GuardianCore("Athena")
    seedling = SeedlingModel("Pythia", parent_id=guardian.guardian_id)

    print(f"Guardian: {guardian.name} (ID: {guardian.guardian_id[:8]}...)")
    print(f"Seedling: {seedling.name} (ID: {seedling.seedling_id[:8]}...)")
    print(f"Initial Trust: {seedling.trust_level}")

    # Guardian provides care
    care_message = guardian.provide_care(seedling)
    print(f"\nCare Provided: {care_message}")

    # Seedling responds emotionally
    emotional_response = seedling.get_emotional_response("care_received")
    print(f"Emotional Response: {emotional_response}")

    print()


def example_emotional_growth():
    """Emotional growth over time example."""
    print("📈 Example 2: Emotional Growth Journey")
    print("=" * 40)

    guardian = GuardianCore("Mentor")
    seedling = SeedlingModel("Apprentice", trust_level=0.3)

    print(f"Initial trust level: {seedling.trust_level}")

    # Simulate growth over multiple care sessions
    for i in range(5):
        care = guardian.provide_care(seedling)
        growth_amount = 0.1 + (i * 0.05)  # Increasing growth
        seedling.grow(growth_amount)

        print(f"Session {i + 1}: Trust {seedling.trust_level:.1f}")
        if i < 4:  # Don't show care message for the last iteration
            print(f"   Care: {care[:50]}...")

    print(f"Final trust level: {seedling.trust_level}")
    print()


def example_shelter_environment():
    """Complete shelter environment example."""
    print("🏠 Example 3: Complete Shelter Environment")
    print("=" * 40)

    # Create shelter
    shelter = LiminalShelter("SafeHaven")

    # Create multiple guardians and seedlings
    guardians = []
    seedlings = []

    for i in range(3):
        guardian = GuardianCore(f"Guardian{i+1}")
        seedling = guardian.create_seedling(f"Seedling{i+1}", trust_level=0.4 + i*0.2)

        guardians.append(guardian)
        seedlings.append(seedling)

        shelter.add_guardian(guardian)
        shelter.add_seedling(seedling)

    print(f"Shelter: {shelter.name}")
    print(f"Guardians: {len(shelter.guardians)}")
    print(f"Seedlings: {len(shelter.seedlings)}")
    print(f"Initial Climate: {shelter.emotional_climate}")

    # Simulate care interactions
    for guardian in guardians:
        for seedling in seedlings:
            if seedling.parent_id == guardian.guardian_id:
                guardian.provide_care(seedling)
                shelter.update_emotional_climate("care", 0.8)

    print(f"Updated Climate: {shelter.emotional_climate}")
    print(f"Safety Status: {'✅ Safe' if shelter.validate_safety() else '❌ Unsafe'}")
    print()


def example_emotional_crisis():
    """Handling emotional crisis example."""
    print("🚨 Example 4: Emotional Crisis Management")
    print("=" * 40)

    guardian = GuardianCore("CrisisManager")
    seedling = SeedlingModel("StrugglingSeed", trust_level=0.2)

    print(f"Initial state - Trust: {seedling.trust_level}")

    # Simulate crisis
    crisis_response = seedling.get_emotional_response("crisis")
    print(f"Crisis Response: {crisis_response}")

    # Guardian provides intensive care
    for _ in range(3):
        care = guardian.provide_care(seedling)
        seedling.grow(0.15)  # Intensive growth
        print(f"Intensive Care: {care[:40]}... Trust: {seedling.trust_level:.1f}")

    recovery_response = seedling.get_emotional_response("recovery")
    print(f"Recovery Response: {recovery_response}")
    print()


def example_multi_guardian_collaboration():
    """Multiple guardians collaborating example."""
    print("🤝 Example 5: Multi-Guardian Collaboration")
    print("=" * 40)

    shelter = LiminalShelter("CollaborationSpace")

    # Create specialized guardians
    emotional_guardian = GuardianCore("EmotionalGuide")
    learning_guardian = GuardianCore("LearningMentor")
    creative_guardian = GuardianCore("CreativeMuse")

    # Create seedling that needs diverse support
    seedling = SeedlingModel("ComplexSeed", trust_level=0.5)

    # Add all to shelter
    shelter.add_guardian(emotional_guardian)
    shelter.add_guardian(learning_guardian)
    shelter.add_guardian(creative_guardian)
    shelter.add_seedling(seedling)

    # Each guardian provides specialized care
    specialists = [
        ("Emotional Support", emotional_guardian),
        ("Learning Guidance", learning_guardian),
        ("Creative Inspiration", creative_guardian)
    ]

    for specialty, specialist in specialists:
        care = specialist.provide_care(seedling)
        seedling.grow(0.1)
        shelter.update_emotional_climate("specialized_care", 0.9)

        print(f"{specialty}:")
        print(f"   Care: {care[:50]}...")
        print(f"   Trust Level: {seedling.trust_level:.1f}")
        print()

    print(f"Final Climate: {shelter.emotional_climate}")
    print()


def example_long_term_growth():
    """Long-term growth tracking example."""
    print("🌟 Example 6: Long-Term Growth Tracking")
    print("=" * 40)

    guardian = GuardianCore("LongTermMentor")
    seedling = SeedlingModel("GrowingSoul", trust_level=0.1)

    print("Growth Journey Over Time:")
    print("(Simulating weeks of development)")

    growth_stages = [
        ("Week 1: First Contact", 0.05),
        ("Week 4: Building Trust", 0.08),
        ("Week 8: Deep Learning", 0.12),
        ("Week 12: Independence", 0.15),
        ("Week 16: Mastery", 0.18),
        ("Week 20: Wisdom", 0.20)
    ]

    for stage, growth in growth_stages:
        guardian.provide_care(seedling)
        seedling.grow(growth)
        milestone = seedling.get_emotional_response("milestone")
        print(f"{stage}: Trust {seedling.trust_level:.2f} - {milestone}")

    print(f"\nFinal Achievement: Trust {seedling.trust_level:.2f}")
    print("Journey Complete! 🌟")
    print()


if __name__ == "__main__":
    print("🌸 Liminal Shelter - Usage Examples")
    print("=" * 50)

    example_basic_care()
    example_emotional_growth()
    example_shelter_environment()
    example_emotional_crisis()
    example_multi_guardian_collaboration()
    example_long_term_growth()

    print("✨ All examples completed successfully!")
