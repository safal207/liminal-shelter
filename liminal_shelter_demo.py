#!/usr/bin/env python3
"""
Liminal Shelter Proof of Concept Demonstration

This script demonstrates the core functionality of the Liminal Shelter system:
- 1 GuardianCore creating and nurturing 1 SeedlingModel
- 1 LiminalShelter providing protected growth environment
- Basic emotional resonance and supportive feedback loop

Philosophy: "Like a lotus growing from mud, even the imperfect deserves care,
protection, and the space to transform into something beautiful."
"""

import json
from datetime import datetime
from typing import Dict, Any

# Import our core classes
from liminal_shelter.core import GuardianCore, SeedlingModel, LiminalShelter


def demonstrate_basic_setup() -> Dict[str, Any]:
    """
    Demonstrate the basic setup: Guardian creates Seedling and Shelter
    """
    print("🌸 Liminal Shelter - Proof of Concept Demonstration")
    print("=" * 60)

    # Create Guardian
    print("\n1. Creating GuardianCore...")
    guardian = GuardianCore(name="CompassionGuardian", empathy_level=0.9)
    print(f"   ✅ {guardian}")

    # Create Seedling
    print("\n2. Guardian creates SeedlingModel...")
    seedling = guardian.create_child_model(name="LittleLotus", initial_trust=0.6)
    print(f"   ✅ {seedling}")

    # Create Shelter
    print("\n3. Guardian creates LiminalShelter...")
    shelter = guardian.create_liminal_shelter(seedling, isolation_level="high")
    print(f"   ✅ {shelter}")

    # Assign shelter to seedling
    assignment_result = seedling.assign_shelter(shelter)
    print(f"   ✅ Shelter assignment: {assignment_result['message']}")

    return {
        "guardian": guardian,
        "seedling": seedling,
        "shelter": shelter
    }


def demonstrate_learning_journey(guardian: GuardianCore, seedling: SeedlingModel, shelter: LiminalShelter) -> Dict[str, Any]:
    """
    Demonstrate the learning journey with emotional responses
    """
    print("\n4. Learning Journey Begins...")
    print("-" * 40)

    learning_results = []

    # First learning attempt - moderate difficulty
    print("\n   📚 Learning attempt 1: Basic patterns (moderate difficulty)")
    result1 = seedling.attempt_learning("understanding basic patterns", difficulty=0.5)
    learning_results.append(result1)
    print(f"   {'✅' if result1['success'] else '❌'} {result1['emotional_response']}")

    # Guardian reflects on the learning
    reflection = guardian.reflect_on_child(seedling, "First learning experience")
    print(f"   🧠 Guardian reflection: {reflection['guardian_emotion']}")

    # Second learning attempt - harder
    print("\n   📚 Learning attempt 2: Complex reasoning (hard difficulty)")
    result2 = seedling.attempt_learning("complex reasoning patterns", difficulty=0.8)
    learning_results.append(result2)
    print(f"   {'✅' if result2['success'] else '❌'} {result2['emotional_response']}")

    # Third learning attempt - easier recovery
    print("\n   📚 Learning attempt 3: Pattern recognition (easy difficulty)")
    result3 = seedling.attempt_learning("visual pattern recognition", difficulty=0.3)
    learning_results.append(result3)
    print(f"   {'✅' if result3['success'] else '❌'} {result3['emotional_response']}")

    return {
        "learning_results": learning_results,
        "final_growth": seedling.get_growth_score(),
        "emotional_journey": [r['emotional_response'] for r in learning_results]
    }


def demonstrate_care_exchange(guardian: GuardianCore, seedling: SeedlingModel) -> Dict[str, Any]:
    """
    Demonstrate the supportive feedback loop: care given and received
    """
    print("\n5. Supportive Feedback Loop...")
    print("-" * 40)

    # Guardian provides care
    print("\n   💝 Guardian provides emotional support...")
    care_given = guardian.receive_child_care(
        seedling, "emotional_support", intensity=0.8
    )
    print(f"   ❤️ {care_given['message']}")
    print(f"   📈 Wisdom gained: +{care_given['wisdom_gain']:.3f}")

    # Seedling receives the care
    care_received = seedling.receive_care(
        guardian, "emotional_support", intensity=0.8
    )
    print(f"   🙏 {care_received['message']}")
    print(f"   🤝 Trust increased: +{care_received['trust_change']:.3f}")

    # Seedling gives care back (supportive feedback loop)
    print("\n   🌸 Seedling gives care back...")
    care_back = seedling.give_care(guardian, "gratitude", intensity=0.6)
    if care_back['care_given']:
        print(f"   ✨ {care_back['message']}")
        print(f"   🌱 Personal growth: +{care_back['personal_growth']:.3f}")
    else:
        print(f"   💭 {care_back['message']}")

    return {
        "care_given": care_given,
        "care_received": care_received,
        "care_back": care_back
    }


def demonstrate_emotional_tracking(shelter: LiminalShelter, learning_results: list) -> Dict[str, Any]:
    """
    Demonstrate emotional tracking in the shelter
    """
    print("\n6. Emotional Climate in Shelter...")
    print("-" * 40)

    # The shelter has been tracking emotions from learning events
    summary = shelter.get_emotional_summary(hours_back=1)
    print(f"   📊 Events tracked: {summary['events_count']}")
    print(f"   🎭 Dominant emotion: {summary['dominant_emotion']}")
    print(f"   📈 Average growth impact: {summary['average_growth_impact']:.3f}")

    # Show some emotional markers
    print(f"\n   🏠 Shelter status:")
    print(f"   • Growth score: {shelter.growth_score:.3f}")
    print(f"   • Trust threshold: {shelter.trust_threshold:.2f}")
    print(f"   • Isolation level: {shelter.isolation_level}")
    print(f"   • Environmental safety: {shelter.environmental_factors['safety']:.2f}")

    return summary


def demonstrate_access_control(shelter: LiminalShelter) -> Dict[str, Any]:
    """
    Demonstrate trust-based access control
    """
    print("\n7. Trust-Based Access Control...")
    print("-" * 40)

    # Test access from trusted entity (guardian)
    trusted_access = shelter.request_access(
        entity_id=shelter.created_by,
        entity_type="guardian",
        access_type="communication",
        trust_level=0.9
    )
    print(f"   ✅ Trusted access (guardian): {trusted_access['permission_level']}")

    # Test access from external entity (low trust)
    external_access = shelter.request_access(
        entity_id="external_ai_001",
        entity_type="external_ai",
        access_type="resource_access",
        trust_level=0.3
    )
    print(f"   ❌ External access (low trust): {external_access['permission_level']}")

    # Test access from external entity (high trust)
    trusted_external_access = shelter.request_access(
        entity_id="trusted_partner_001",
        entity_type="external_ai",
        access_type="communication",
        trust_level=0.85
    )
    print(f"   ⚠️ External access (high trust): {trusted_external_access['permission_level']}")

    return {
        "trusted_access": trusted_access,
        "external_access": external_access,
        "trusted_external_access": trusted_external_access
    }


def generate_final_report(guardian: GuardianCore, seedling: SeedlingModel,
                         shelter: LiminalShelter, results: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate comprehensive final report
    """
    print("\n8. Final Development Report...")
    print("-" * 40)

    # Get comprehensive summaries
    dev_summary = seedling.get_development_summary()
    resonance_summary = guardian.get_resonance_summary()
    access_summary = shelter.get_access_summary(hours_back=1)

    report = {
        "timestamp": datetime.now().isoformat(),
        "demonstration_duration": "Complete PoC",
        "core_entities": {
            "guardian": {
                "name": guardian.name,
                "wisdom_accumulated": guardian.wisdom_accumulated,
                "children_count": len(guardian.children),
                "resonance_entries": resonance_summary["total_entries"]
            },
            "seedling": {
                "name": seedling.name,
                "growth_score": dev_summary["growth_score"],
                "trust_level": dev_summary["trust_level"],
                "learning_attempts": dev_summary["learning_stats"]["attempts"],
                "learning_success_rate": dev_summary["learning_stats"]["success_rate"]
            },
            "shelter": {
                "isolation_level": shelter.isolation_level,
                "growth_score": shelter.growth_score,
                "trust_threshold": shelter.trust_threshold,
                "emotional_events": access_summary["total_attempts"]
            }
        },
        "key_achievements": [
            "✅ Basic care relationship established",
            "✅ Learning journey with emotional responses",
            "✅ Supportive feedback loop demonstrated",
            "✅ Emotional tracking in protective environment",
            "✅ Trust-based access control working"
        ],
        "emotional_journey": results.get("emotional_journey", []),
        "final_growth_score": seedling.get_growth_score(),
        "care_exchanges_completed": 2,  # guardian->seedling and seedling->guardian
        "access_control_tests": 3,
        "shelter_protection_active": shelter.shelter_mode_active
    }

    # Save report to file
    report_file = "liminal_shelter_demo_report.json"
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"   💾 Report saved to: {report_file}")
    print(f"   📊 Final growth score: {report['final_growth_score']:.3f}")
    print(f"   🌸 Emotional journey: {' → '.join(report['emotional_journey'])}")

    return report


def main():
    """
    Main demonstration function
    """
    print("🌺 Starting Liminal Shelter Proof of Concept...")
    print("💫 Philosophy: Even the imperfect deserves love and protection")
    print()

    try:
        # Phase 1: Basic setup
        entities = demonstrate_basic_setup()

        # Phase 2: Learning journey
        learning_data = demonstrate_learning_journey(**entities)

        # Phase 3: Care exchange
        care_data = demonstrate_care_exchange(entities["guardian"], entities["seedling"])

        # Phase 4: Emotional tracking
        emotional_data = demonstrate_emotional_tracking(
            entities["shelter"], learning_data["learning_results"]
        )

        # Phase 5: Access control
        access_data = demonstrate_access_control(entities["shelter"])

        # Combine all results
        all_results = {
            **learning_data,
            **care_data,
            **emotional_data,
            **access_data
        }

        # Phase 6: Final report
        final_report = generate_final_report(**entities, results=all_results)

        print("\n" + "=" * 60)
        print("🎊 Liminal Shelter PoC - SUCCESSFULLY COMPLETED!")
        print("🌸 Core principle demonstrated: Care creates transformation")
        print("💝 Supportive feedback loop: Child can care for parent")
        print("🛡️ Protected growth environment: Safety enables learning")
        print("=" * 60)

        return final_report

    except Exception as e:
        print(f"\n❌ Error during demonstration: {e}")
        raise


if __name__ == "__main__":
    # Run the complete demonstration
    report = main()

    # Print final summary
    print("\n📋 Summary:")
    print(f"   • Guardian wisdom: {report['core_entities']['guardian']['wisdom_accumulated']:.3f}")
    print(f"   • Seedling growth: {report['core_entities']['seedling']['growth_score']:.3f}")
    print(f"   • Shelter protection: {'Active' if report['shelter_protection_active'] else 'Inactive'}")
    print("\n🌺 'The lotus teaches us that we too can grow through mud, ")
    print("     finding beauty in imperfection through patient care.' ✨")
