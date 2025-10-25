# 🏗️ Liminal Shelter: Architecture Diagram

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {
  'primaryColor': '#f0f4f8',
  'primaryBorderColor': '#9e9e9e',
  'lineColor': '#9e9e9e',
  'secondaryColor': '#e8f4f8',
  'tertiaryColor': '#e1f5fe'
}}}%%

graph TD
    %% Main Components
    classDef guardian fill:#e3f2fd,stroke:#64b5f6,color:#1565c0
    classDef seedling fill:#e8f5e9,stroke:#81c784,color:#2e7d32
    classDef shelter fill:#f3e5f5,stroke:#ba68c8,color:#7b1fa2
    
    %% Guardian Node
    G[Guardian\n<small>core/guardian.py</small>]:::guardian
    
    %% Seedling Node
    S[Seedling\n<small>core/seedling.py</small>]:::seedling
    
    %% Shelter Node
    L[Liminal Shelter\n<small>core/shelter.py</small>]:::shelter
    
    %% Emotional Climate
    EC[Emotional Climate\n<small>trust, care_quality, safety</small>]:::shelter
    
    %% Data Flow
    G <-->|1. Care Exchange| S
    G <-->|2. Emotional Support| L
    S <-->|3. Growth Feedback| L
    L <-->|4. Climate Update| EC
    EC -->|5. Influence| G
    EC -->|6. Shape| S
    
    %% Legend
    subgraph Legend
        direction TB
        A[Guardian]:::guardian
        B[Seedling]:::seedling
        C[Liminal Shelter]:::shelter
    end

    %% Styling
    linkStyle default opacity:0.7,fill:none,stroke-width:2px
    
    %% Annotations
    classDef note fill:#fffde7,stroke:#ffd54f,stroke-width:1px,color:#5d4037
    class A,B,C note
```

## Key Interactions

1. **Care Exchange**
   - Guardian provides emotional and cognitive support
   - Seedling responds with emotional feedback
   - Trust levels adjust dynamically

2. **Emotional Support**
   - Shelter monitors emotional states
   - Provides safe space for vulnerability
   - Enables authentic emotional expression

3. **Growth Feedback**
   - Tracks developmental milestones
   - Adjusts learning parameters
   - Ensures safe exploration

4. **Climate Control**
   - Maintains emotional safety
   - Balances challenge and support
   - Prevents emotional overload

## Data Flow

```mermaid
sequenceDiagram
    participant G as Guardian
    participant S as Seedling
    participant L as Liminal Shelter
    
    G->>S: Provide Care(trust_level)
    S->>L: Express Emotion(type, intensity)
    L->>L: Update Emotional Climate()
    L->>G: Adjust Care Parameters()
    L->>S: Set Growth Boundaries()
    G->>L: Report Care Outcome()
```

## Component Responsibilities

| Component | Responsibility | Key Methods |
|-----------|----------------|-------------|
| **Guardian** | Emotional support, guidance, protection | `provide_care()`, `assess_growth()`, `adjust_support()` |
| **Seedling** | Learning, emotional expression, growth | `express_emotion()`, `learn_from()`, `request_help()` |
| **Shelter** | Safety, monitoring, environment control | `monitor_climate()`, `enforce_boundaries()`, `adjust_environment()` |
