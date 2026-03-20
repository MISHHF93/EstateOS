const journeys = {
  buyer: {
    title: "Buyer journey",
    summary: "Balanced recommendations for livability, affordability, relocation readiness, and transaction certainty.",
    confidence: 0.94,
    releaseStatus: "Ready with transaction review",
    headline: "Personalized shortlist shaped by property, finance, visa, insurance, pricing, and transaction experts",
    subtitle: "The workspace keeps property guidance and deal execution in the same flow so users can see what happens next.",
    steps: [
      "Capture investor type, relocation timeline, budget, and privacy preferences from the adaptive intake panel.",
      "Route the request through property, finance, visa, insurance, pricing, and transaction-risk experts based on stated goals.",
      "Rank candidate properties by fit, risk, residency alignment, and closing readiness instead of price alone.",
      "Release only policy-cleared recommendations with clear reasons, document status, and next-best actions."
    ],
    profile: {
      investorType: "Owner-occupier",
      location: "United States → Portugal",
      financialIntent: "Primary residence with moderate appreciation",
      residencyGoal: "Family relocation in 12 months",
      access: "Client RBAC • MFA on release"
    },
    defaults: {
      objective: "relocate",
      risk: "balanced",
      explanationDepth: "guided",
      budget: 650000,
      residency: true,
      financing: true
    },
    objectives: [
      { value: "relocate", label: "Relocate with confidence" },
      { value: "stability", label: "Prioritize stability" },
      { value: "lifestyle", label: "Lifestyle-led search" }
    ],
    candidates: [
      {
        id: "lisbon-green",
        title: "Lisbon Green Quarter Apartment",
        location: "Lisbon, Portugal",
        price: 620000,
        summary: "Transit-friendly two-bedroom home with retrofit upside and family-ready amenities.",
        tags: ["Walkable district", "School access", "Energy retrofit eligible"],
        experts: { property: 0.93, investment: 0.72, visa: 0.9, insurance: 0.84, finance: 0.82, compliance: 0.95 },
        climateRisk: "low",
        financingFit: 0.84,
        visaPathway: {
          title: "Portugal D7 / family relocation route",
          fit: "Strong",
          summary: "Best when the family plans residency with recurring income and wants straightforward documentation."
        },
        insurance: {
          title: "Home + contents + legal protection",
          premium: "$188/mo estimated",
          summary: "Low peril concentration and strong building profile produce fast underwriting readiness."
        },
        insight: "Higher livability and relocation support than pure yield alternatives.",
        why: "Ranks first because it balances everyday usability, financing readiness, and visa alignment without meaningful climate friction."
      },
      {
        id: "cascais-coast",
        title: "Cascais Coastal Townhome",
        location: "Cascais, Portugal",
        price: 780000,
        summary: "Lifestyle-forward family townhome with stronger appreciation upside and premium coastal demand.",
        tags: ["Premium district", "Coastal demand", "Strong resale appeal"],
        experts: { property: 0.88, investment: 0.77, visa: 0.86, insurance: 0.68, finance: 0.69, compliance: 0.94 },
        climateRisk: "medium",
        financingFit: 0.68,
        visaPathway: {
          title: "Portugal D7 / lifestyle relocation route",
          fit: "Good",
          summary: "Suitable for households optimizing lifestyle quality, but insurance and budget pressure are higher."
        },
        insurance: {
          title: "Enhanced coastal property cover",
          premium: "$264/mo estimated",
          summary: "Wind and salt-air exposure increase premium and documentation requirements."
        },
        insight: "Good appreciation narrative, but less forgiving under tighter financing scenarios.",
        why: "Strong neighborhood desirability is partially offset by insurance drag and lower affordability resilience."
      },
      {
        id: "porto-riverside",
        title: "Porto Riverside Loft",
        location: "Porto, Portugal",
        price: 540000,
        summary: "Lower entry cost and resilient rental support for buyers who want flexibility over prestige.",
        tags: ["Lower acquisition cost", "Rental fallback", "Transit access"],
        experts: { property: 0.81, investment: 0.76, visa: 0.82, insurance: 0.83, finance: 0.88, compliance: 0.93 },
        climateRisk: "low",
        financingFit: 0.9,
        visaPathway: {
          title: "Portugal D7 / flexible living route",
          fit: "Good",
          summary: "Works well when affordability and optional rental income are more important than prestige."
        },
        insurance: {
          title: "Standard property protection package",
          premium: "$171/mo estimated",
          summary: "Low hazard complexity keeps coverage affordable and easy to place."
        },
        insight: "Financial resilience is strongest here, though lifestyle fit is slightly weaker for family relocation.",
        why: "Strong affordability and insurance fit lift the score, but the family-use experience is less tailored than Lisbon."
      }
    ],
    nextActions: [
      "Schedule pre-qualification and collect proof-of-income documents.",
      "Open the residency checklist for dependents and timeline planning.",
      "Request bundled home insurance and legal protection estimates."
    ],
    deal: {
      name: "Lisbon Green Quarter acquisition",
      summary: "Buyer-side transaction workspace tracks the offer, seller response window, open document exceptions, and continuity posture before closing.",
      riskLabel: "Moderate risk",
      targetPrice: 598000,
      closeWindow: "18 business days",
      integrity: "In sequence",
      continuityMode: "Active-active failover",
      stages: [
        { stage: "Intake", status: "completed", progress: 100, owner: "Buyer ops", note: "Identity and consent bound to the deal." },
        { stage: "Pricing review", status: "completed", progress: 100, owner: "Deal desk", note: "Offer ladder approved for controlled concessions." },
        { stage: "Negotiation", status: "in progress", progress: 74, owner: "Advisor", note: "Seller response deadline in 36 hours." },
        { stage: "Document validation", status: "in progress", progress: 68, owner: "Legal", note: "Permit attachment still missing from disclosure pack." },
        { stage: "Approval", status: "pending", progress: 22, owner: "Transaction manager", note: "Legal sign-off required before release." },
        { stage: "Closing", status: "pending", progress: 0, owner: "Closing agent", note: "Continuity playbook already attached." }
      ],
      experts: [
        { title: "Pricing strategy", status: "High priority", score: 0.88, summary: "Anchor at $598k, keep concessions tied to permit remediation, and preserve a documented walk-away threshold." },
        { title: "Negotiation insight", status: "High priority", score: 0.81, summary: "Use the open disclosure item as leverage and hold deadline-backed counters instead of broad concessions." },
        { title: "Document validation", status: "Critical", score: 0.72, summary: "Only one blocker remains, but closing should stay gated until the renovation permit is attached and re-validated." },
        { title: "Deal risk scoring", status: "Monitor", score: 0.69, summary: "Risk remains manageable because financing and title are clean, but counterparty delay could widen the close window." }
      ],
      documents: [
        { name: "Title and encumbrance report", status: "Validated", owner: "Legal counsel", note: "No encumbrance exceptions detected." },
        { name: "Seller disclosure package", status: "Needs review", owner: "Broker", note: "Renovation permit attachment missing from the signed packet." },
        { name: "Lender commitment letter", status: "Validated", owner: "Lender", note: "Commitment aligns with the modeled leverage plan." }
      ],
      controls: [
        { control: "ISO/IEC 27001 access governance", status: "Active", detail: "RBAC, MFA, and approval segregation are active for pricing and release actions." },
        { control: "ISO 22301 continuity mode", status: "Active", detail: "Deal events are replayable and closing can fail over to the backup queue if the primary workflow stalls." },
        { control: "Immutable audit evidence", status: "Active", detail: "All counters, stage updates, and validation outcomes are written to the evidence ledger." },
        { control: "Document completeness gate", status: "Review", detail: "Closing remains gated until the seller disclosure package is fully validated." }
      ]
    }
  },
  investor: {
    title: "Investor journey",
    summary: "Ranked opportunities optimized for yield, resilience, optional residency pathways, and transaction discipline.",
    confidence: 0.92,
    releaseStatus: "Reviewable with advisor",
    headline: "Portfolio-style comparison that blends return, jurisdiction, negotiation posture, and diligence signals",
    subtitle: "Investors get richer downside framing and stage-aware controls before capital is committed.",
    steps: [
      "Capture return goals, hold period, cross-border intent, and diversification preferences.",
      "Aggregate investment, pricing, visa, insurance, finance, and compliance outputs into one ranking model.",
      "Explain which expert signals lifted or lowered each candidate instead of presenting a black-box score.",
      "Escalate medium-risk cases to advisor review before export, offer submission, or partner actions."
    ],
    profile: {
      investorType: "Cross-border investor",
      location: "United States → UAE / Greece / Portugal",
      financialIntent: "Income plus long-term appreciation",
      residencyGoal: "Optional second residency",
      access: "Investor RBAC • MFA on export"
    },
    defaults: {
      objective: "yield",
      risk: "balanced",
      explanationDepth: "detailed",
      budget: 950000,
      residency: true,
      financing: false
    },
    objectives: [
      { value: "yield", label: "Maximize yield" },
      { value: "diversify", label: "Diversify markets" },
      { value: "residency", label: "Keep residency optional" }
    ],
    candidates: [
      {
        id: "athens-urban",
        title: "Athens Urban Residential Block",
        location: "Athens, Greece",
        price: 880000,
        summary: "Diversified multifamily-style opportunity with strong occupancy support and moderate entry cost.",
        tags: ["Rental demand", "Portfolio diversification", "Mid-volatility market"],
        experts: { property: 0.86, investment: 0.91, visa: 0.82, insurance: 0.8, finance: 0.85, compliance: 0.94 },
        climateRisk: "medium",
        financingFit: 0.84,
        visaPathway: {
          title: "Greece Golden Visa adjacent pathway",
          fit: "Good",
          summary: "Useful for optional residency, but policy monitoring is advised due to program evolution."
        },
        insurance: {
          title: "Landlord + catastrophe buffer package",
          premium: "$322/mo estimated",
          summary: "Coverage remains accessible with earthquake and liability extensions."
        },
        insight: "Best blend of yield, occupancy resilience, and diversification for the modeled budget.",
        why: "Top-ranked because investment and finance experts strongly favor downside resilience while visa and insurance remain workable."
      },
      {
        id: "dubai-marina",
        title: "Dubai Marina Branded Residence",
        location: "Dubai, UAE",
        price: 1200000,
        summary: "Premium asset with high upside and liquidity, but more cyclical pricing and premium insurance costs.",
        tags: ["Prestige asset", "Liquidity", "FX sensitivity"],
        experts: { property: 0.9, investment: 0.88, visa: 0.87, insurance: 0.73, finance: 0.74, compliance: 0.92 },
        climateRisk: "medium",
        financingFit: 0.71,
        visaPathway: {
          title: "UAE investor residence route",
          fit: "Strong",
          summary: "Residency fit is attractive, especially for globally mobile investors with premium budgets."
        },
        insurance: {
          title: "High-value property cover",
          premium: "$418/mo estimated",
          summary: "Premium profile and property value raise annual carrying cost and documentation expectations."
        },
        insight: "Upside is strong, but FX and premium carry reduce resilience under slower growth conditions.",
        why: "Strong property and visa signals are offset by softer finance and insurance scores at the target budget."
      },
      {
        id: "lisbon-income",
        title: "Lisbon Urban Rental Pair",
        location: "Lisbon, Portugal",
        price: 760000,
        summary: "Two smaller assets designed for balanced income and optional future owner use.",
        tags: ["Income diversification", "Flexible exit", "Moderate policy risk"],
        experts: { property: 0.84, investment: 0.87, visa: 0.78, insurance: 0.82, finance: 0.86, compliance: 0.95 },
        climateRisk: "low",
        financingFit: 0.86,
        visaPathway: {
          title: "Portugal residency-adjacent route",
          fit: "Moderate",
          summary: "Residency is less central here, but the holding still works well for optional relocation later."
        },
        insurance: {
          title: "Portfolio landlord package",
          premium: "$296/mo estimated",
          summary: "Balanced coverage profile with manageable exclusions and quick placement."
        },
        insight: "Strong on flexibility and financing efficiency, weaker on immediate residency value.",
        why: "A close second when optionality matters more than prestige or headline upside."
      }
    ],
    nextActions: [
      "Review downside cases with an advisor before any export or partner submission.",
      "Open FX and leverage sensitivity analysis for the top two assets.",
      "Start residency evidence collection only for markets that remain top-ranked after diligence."
    ],
    deal: {
      name: "Athens Urban Block diligence",
      summary: "Investor transaction view emphasizes negotiation leverage, diligence checklist quality, and capital-at-risk controls before commitment.",
      riskLabel: "High review",
      targetPrice: 845000,
      closeWindow: "24 business days",
      integrity: "In sequence",
      continuityMode: "Warm standby + replay",
      stages: [
        { stage: "Intake", status: "completed", progress: 100, owner: "Investor ops", note: "Entity structure and beneficial owners captured." },
        { stage: "Pricing review", status: "completed", progress: 100, owner: "Investment committee", note: "Bid range set around downside yield guardrails." },
        { stage: "Negotiation", status: "in progress", progress: 61, owner: "Advisor", note: "Seller pushing for fewer financing contingencies." },
        { stage: "Document validation", status: "in progress", progress: 49, owner: "Legal", note: "Tenant roster and one inspection report still under review." },
        { stage: "Approval", status: "pending", progress: 15, owner: "IC chair", note: "Approval waits for diligence exceptions to close." },
        { stage: "Closing", status: "pending", progress: 0, owner: "Local counsel", note: "Fallback workflow ready if seller timeline compresses." }
      ],
      experts: [
        { title: "Pricing strategy", status: "High priority", score: 0.84, summary: "Keep the bid near $845k and tie any upward movement to verified occupancy and inspection evidence." },
        { title: "Negotiation insight", status: "High priority", score: 0.78, summary: "Trade certainty for price only after tenant roster inconsistencies are resolved and recorded." },
        { title: "Document validation", status: "Critical", score: 0.66, summary: "The open inspection and tenant-data issues materially affect diligence quality and should block final approval." },
        { title: "Deal risk scoring", status: "Escalate", score: 0.62, summary: "Risk is elevated because incomplete diligence and seller pressure could erode downside protection." }
      ],
      documents: [
        { name: "Occupancy and tenant roster", status: "Needs review", owner: "Seller counsel", note: "Unit-level lease metadata does not fully reconcile." },
        { name: "Inspection report", status: "Needs review", owner: "Inspector", note: "Supplemental structure notes due tomorrow." },
        { name: "Entity KYC package", status: "Validated", owner: "Compliance", note: "Beneficial ownership evidence approved." }
      ],
      controls: [
        { control: "ISO/IEC 27001 access governance", status: "Active", detail: "Investment committee, advisor, and legal roles are segregated for approval decisions." },
        { control: "ISO 22301 continuity mode", status: "Active", detail: "Deal workflow can replay from event history and move to the backup queue if the seller accelerates closing." },
        { control: "Immutable audit evidence", status: "Active", detail: "Bid updates and diligence exceptions are chained into a tamper-evident ledger." },
        { control: "Document completeness gate", status: "Review", detail: "Final approval remains blocked until tenant and inspection exceptions are cleared." }
      ]
    }
  },
  advisor: {
    title: "Advisor console",
    summary: "Evidence-first oversight that exposes ranking logic, policy outcomes, and release-ready transaction guidance.",
    confidence: 0.96,
    releaseStatus: "Approval-ready",
    headline: "Advisor view optimized for challenge, endorsement, and documented human oversight across deals",
    subtitle: "The workspace expands explanation depth and surfaces stage controls, approvals, and audit evidence by default.",
    steps: [
      "Inspect profile context, policy posture, and expert outputs in a single evidence panel.",
      "Compare ranked property options and supporting visa, finance, transaction, and insurance narratives side by side.",
      "Review why the top recommendation won, which expert signals contributed, and what should be challenged.",
      "Approve, request more evidence, or hold release while preserving an auditable decision trail."
    ],
    profile: {
      investorType: "Advisor-managed portfolio",
      location: "Global client coverage",
      financialIntent: "Suitability and portfolio oversight",
      residencyGoal: "Jurisdiction-specific advisory",
      access: "Advisor RBAC • Entitled approval"
    },
    defaults: {
      objective: "suitability",
      risk: "conservative",
      explanationDepth: "full",
      budget: 1100000,
      residency: true,
      financing: false
    },
    objectives: [
      { value: "suitability", label: "Prioritize suitability" },
      { value: "evidence", label: "Evidence deep dive" },
      { value: "approval", label: "Prepare release memo" }
    ],
    candidates: [
      {
        id: "barcelona-family-office",
        title: "Barcelona Family Office Residence",
        location: "Barcelona, Spain",
        price: 1050000,
        summary: "Premium family-use asset with strong advisory narrative and clean documentation footprint.",
        tags: ["High documentation quality", "Client-friendly narrative", "Moderate downside"],
        experts: { property: 0.87, investment: 0.79, visa: 0.75, insurance: 0.85, finance: 0.83, compliance: 0.97 },
        climateRisk: "medium",
        financingFit: 0.82,
        visaPathway: {
          title: "Spain residence planning review",
          fit: "Conditional",
          summary: "Requires current legal review, but remains useful for advisory pathway mapping."
        },
        insurance: {
          title: "Premium residence and liability cover",
          premium: "$352/mo estimated",
          summary: "Straightforward underwriting with premium contents and legal liability add-ons."
        },
        insight: "Best advisory fit when the client values a stable story, documentation quality, and controlled downside.",
        why: "Compliance strength and clean client narrative outweigh the softer visa fit in this advisory scenario."
      },
      {
        id: "athens-balanced",
        title: "Athens Balanced Income Asset",
        location: "Athens, Greece",
        price: 890000,
        summary: "Balanced option with strong yield support and clearer residency framing for clients seeking optionality.",
        tags: ["Client optionality", "Yield support", "Policy watchlist"],
        experts: { property: 0.84, investment: 0.88, visa: 0.83, insurance: 0.79, finance: 0.82, compliance: 0.94 },
        climateRisk: "medium",
        financingFit: 0.82,
        visaPathway: {
          title: "Greece residency planning",
          fit: "Good",
          summary: "Useful pathway if the client wants optional residency alongside an income case."
        },
        insurance: {
          title: "Residential income + catastrophe rider",
          premium: "$314/mo estimated",
          summary: "Slightly more coverage complexity, but still acceptable for release."
        },
        insight: "A better fit than Barcelona when visa optionality matters more than client-story simplicity.",
        why: "Investment and visa experts push this upward, but compliance confidence is marginally lower than Barcelona."
      },
      {
        id: "dubai-premium",
        title: "Dubai Premium Diversifier",
        location: "Dubai, UAE",
        price: 1450000,
        summary: "High-upside recommendation for aggressive clients comfortable with premium carry and market cyclicality.",
        tags: ["Premium upside", "Higher carry", "Aggressive profile only"],
        experts: { property: 0.9, investment: 0.86, visa: 0.88, insurance: 0.7, finance: 0.68, compliance: 0.93 },
        climateRisk: "medium",
        financingFit: 0.65,
        visaPathway: {
          title: "UAE investor route",
          fit: "Strong",
          summary: "Attractive for mobility, but only suitable for clients with premium budgets and tolerance for carry."
        },
        insurance: {
          title: "High-value diversified cover",
          premium: "$449/mo estimated",
          summary: "More expensive and less forgiving under tighter suitability constraints."
        },
        insight: "Advisable only for clients who explicitly accept cyclical exposure and premium operating costs.",
        why: "Ranks lower because suitability controls penalize the heavier budget and carry profile in advisor mode."
      }
    ],
    nextActions: [
      "Confirm policy versioning and attach supporting evidence before release.",
      "Open the explanation ledger in full mode for client-facing memo preparation.",
      "Document any override rationale if the top-ranked option is not selected."
    ],
    deal: {
      name: "Barcelona advisory release memo",
      summary: "Advisor transaction mode emphasizes documented oversight, approval sequencing, document quality, and resilience evidence before client release.",
      riskLabel: "Low risk",
      targetPrice: 1015000,
      closeWindow: "12 business days",
      integrity: "Approval-ready",
      continuityMode: "Tier 1 active-active",
      stages: [
        { stage: "Intake", status: "completed", progress: 100, owner: "Advisor ops", note: "Client suitability context bound to the case." },
        { stage: "Pricing review", status: "completed", progress: 100, owner: "Deal committee", note: "Defensible pricing memo and alternate scenarios approved." },
        { stage: "Negotiation", status: "completed", progress: 100, owner: "Advisor", note: "Terms accepted with clear fallback clauses." },
        { stage: "Document validation", status: "completed", progress: 100, owner: "Legal", note: "Signatures, disclosures, and title evidence validated." },
        { stage: "Approval", status: "in progress", progress: 88, owner: "Approver", note: "Final memo assembly and override review underway." },
        { stage: "Closing", status: "pending", progress: 34, owner: "Closing counsel", note: "Continuity and client communication playbooks attached." }
      ],
      experts: [
        { title: "Pricing strategy", status: "Medium priority", score: 0.9, summary: "Current negotiated price is already within the defensible valuation corridor, so focus shifts to term certainty." },
        { title: "Negotiation insight", status: "Medium priority", score: 0.87, summary: "Preserve the accepted fallback clauses and keep memo language aligned with documented concessions." },
        { title: "Document validation", status: "Resolved", score: 0.95, summary: "All required diligence and release artifacts are validated and linked to the evidence bundle." },
        { title: "Deal risk scoring", status: "Low", score: 0.89, summary: "Risk is low because workflow sequencing, approvals, and documentation are clean and replayable." }
      ],
      documents: [
        { name: "Title and registry report", status: "Validated", owner: "Legal counsel", note: "Registry evidence attached to the release bundle." },
        { name: "Client suitability memo", status: "Validated", owner: "Advisor", note: "Memo aligned with selected recommendation and override policy." },
        { name: "Closing checklist", status: "Validated", owner: "Closing counsel", note: "Continuity and communication steps embedded." }
      ],
      controls: [
        { control: "ISO/IEC 27001 access governance", status: "Active", detail: "Approver and preparer responsibilities are segregated with MFA-backed sign-off." },
        { control: "ISO 22301 continuity mode", status: "Active", detail: "Client release and closing workflows have alternate routing and replayable event history." },
        { control: "Immutable audit evidence", status: "Active", detail: "Recommendation rationale, approvals, and release memo changes are tamper-evident." },
        { control: "Document completeness gate", status: "Active", detail: "All required artifacts are validated and closing can proceed when approvals finalize." }
      ]
    }
  }
};

const expertMeta = {
  property: { label: "Property expert", icon: "Property" },
  investment: { label: "Investment expert", icon: "Investment" },
  visa: { label: "Visa expert", icon: "Visa" },
  insurance: { label: "Insurance expert", icon: "Insurance" },
  finance: { label: "Finance expert", icon: "Finance" },
  compliance: { label: "Unified compliance & risk expert", icon: "Compliance" },
  recommendation: { label: "Recommendation expert", icon: "Recommend" }
};

const propertyIntelligence = {
  "lisbon-green": {
    valuationBand: "$600k-$645k",
    comparables: "Three central Lisbon family apartment comparables support the range.",
    trend: "Stable family-demand momentum with constrained supply.",
    location: "Walkability, school access, and low-friction transit lift long-term fit.",
    rationale: "The recommendation expert prefers this listing because value confidence and household fit align best."
  },
  "cascais-coast": {
    valuationBand: "$745k-$805k",
    comparables: "Premium coastal townhome comps are supportive but more variable on carrying cost.",
    trend: "Healthy premium demand with greater macro sensitivity.",
    location: "Lifestyle appeal is excellent, though coastal exposure adds friction.",
    rationale: "The recommendation expert penalizes insurance drag and budget stretch relative to Lisbon."
  },
  "porto-riverside": {
    valuationBand: "$520k-$555k",
    comparables: "Riverfront loft comps and rent-support evidence create a tight entry range.",
    trend: "Moderate appreciation with stronger affordability retention.",
    location: "Transit and rental fallback improve flexibility over prestige-led options.",
    rationale: "The recommendation expert keeps this near the top because financing resilience is strongest."
  },
  "athens-urban": {
    valuationBand: "$845k-$910k",
    comparables: "Comparable residential blocks and stabilized rent rolls support the value case.",
    trend: "Yield-led demand remains constructive in a mid-volatility market.",
    location: "Dense urban amenities and occupancy drivers improve resilience.",
    rationale: "The recommendation expert ranks this first for investor fit due to yield and diversification strength."
  },
  "dubai-marina": {
    valuationBand: "$1.16M-$1.24M",
    comparables: "Premium branded residence comps confirm upside with wider premium-market dispersion.",
    trend: "Momentum is favorable but more cyclical under FX or rate shocks.",
    location: "Liquidity and prestige are strong, while carry costs are highest.",
    rationale: "The recommendation expert lowers the rank because premium carry weakens resilience."
  },
  "lisbon-income": {
    valuationBand: "$735k-$785k",
    comparables: "Two-unit rental comps show stable income pricing with manageable vacancy assumptions.",
    trend: "Balanced market momentum with moderate policy watchpoints.",
    location: "Flexible exit paths and central access support future optionality.",
    rationale: "The recommendation expert values flexibility and capital efficiency, keeping this close to first."
  },
  "barcelona-family-office": {
    valuationBand: "$1.01M-$1.08M",
    comparables: "Premium residence comparables support the price with strong documentation quality.",
    trend: "Steady prime-market demand with controlled downside.",
    location: "Dense services and narrative clarity improve advisor confidence.",
    rationale: "The recommendation expert favors this option because it is easiest to defend in a suitability memo."
  },
  "athens-balanced": {
    valuationBand: "$860k-$915k",
    comparables: "Comparable income assets and rent comps support a balanced valuation case.",
    trend: "Healthy income demand with moderate policy-watch exposure.",
    location: "Residency optionality and urban access strengthen client flexibility.",
    rationale: "The recommendation expert keeps this close because yield and residency optionality are both strong."
  },
  "dubai-premium": {
    valuationBand: "$1.39M-$1.49M",
    comparables: "High-end comparables support the range but with broader volatility bands.",
    trend: "Premium growth potential is strong, but cyclicality is higher.",
    location: "Global mobility is attractive, though cost-to-fit is weakest for conservative advice.",
    rationale: "The recommendation expert places it last because suitability and carrying cost outweigh upside here."
  }
};

const residencyPrograms = {
  Portugal: {
    program: "Portugal D7 Residency",
    pathwayType: "Passive-income residency",
    minimumPropertyValue: 0,
    minimumAnnualIncome: 12000,
    minimumLiquidAssets: 36000,
    documents: ["Passport", "Proof of income", "Bank statements", "Health insurance", "Criminal record", "Proof of address"],
    reviewDocuments: ["Portuguese tax number", "Lease or property deed", "Family dependents pack"],
    workflow: [
      "KYC identity verification",
      "AML source-of-funds review",
      "Document authenticity validation",
      "Privacy minimization and consent logging",
      "Counsel filing review"
    ],
    notes: "Property helps the file but recurring income and accommodation evidence remain the core gate."
  },
  Greece: {
    program: "Greece Golden Visa",
    pathwayType: "Property-led residency",
    minimumPropertyValue: 250000,
    minimumAnnualIncome: 0,
    minimumLiquidAssets: 50000,
    documents: ["Passport", "Property purchase agreement", "Proof of funds", "Health insurance", "Criminal record"],
    reviewDocuments: ["Land registry extract", "Greek tax number", "Family dependents pack"],
    workflow: [
      "KYC identity verification",
      "AML source-of-funds review",
      "Property title and valuation validation",
      "Privacy minimization and consent logging",
      "Compliance sign-off before filing"
    ],
    notes: "Property value and own-funds traceability are the main automated checks before counsel review."
  },
  UAE: {
    program: "UAE Property Investor Visa",
    pathwayType: "Property investor residence",
    minimumPropertyValue: 205000,
    minimumAnnualIncome: 0,
    minimumLiquidAssets: 75000,
    documents: ["Passport", "Property title deed", "Proof of funds", "Health insurance", "Bank statements"],
    reviewDocuments: ["Emirates ID application pack", "Utility bill", "Family dependents pack"],
    workflow: [
      "KYC identity verification",
      "AML source-of-funds review",
      "Property ownership confirmation",
      "Privacy minimization and consent logging",
      "Operational visa issuance handoff"
    ],
    notes: "Higher property values can improve pathway strength, but title deed quality and source-of-funds evidence are usually decisive."
  }
};

const insuranceProfiles = {
  buyer: {
    profileLabel: "Owner-occupied family home",
    secureExchange: "ACORD 80 homeowners intake + ACORD 28 evidence summary",
    controls: [
      "NAIC model-law aligned privacy notice and consent receipt before quote request.",
      "Carrier data exchange is minimized to occupancy, construction, hazard, and mortgage fields required for underwriting.",
      "Quote release requires MFA-backed identity, encrypted payload delivery, and immutable servicing logs."
    ],
    options: {
      condo: {
        homeowners: {
          title: "HO-6 homeowners + contents protection",
          fit: "Primary recommendation",
          premium: "$146/mo est.",
          summary: "Best for owner-occupied condos where interior improvements, contents, and loss-of-use need to sit alongside association coverage."
        },
        titlePolicy: {
          title: "Owner's title insurance",
          fit: "Recommended at closing",
          premium: "$1,950 one-time est.",
          summary: "Protects against title defects, recording errors, and unknown encumbrances before transfer completes."
        },
        landlord: {
          title: "Deferred landlord endorsement",
          fit: "Only if future rental is planned",
          premium: "$38/mo add-on est.",
          summary: "Useful when the buyer may convert the unit into a rental after residency or relocation changes."
        },
        life: {
          title: "Level-term life / mortgage continuity cover",
          fit: "Recommended for financed households",
          premium: "$52/mo est.",
          summary: "Creates payment continuity for dependents when the purchase relies on household income."
        }
      },
      single_family: {
        homeowners: {
          title: "HO-3 homeowners + contents + liability",
          fit: "Primary recommendation",
          premium: "$188/mo est.",
          summary: "Broad dwelling, contents, liability, and additional living expense protection fits family owner-occupiers best."
        },
        titlePolicy: {
          title: "Owner's + enhanced title bundle",
          fit: "Recommended at closing",
          premium: "$2,280 one-time est.",
          summary: "Adds stronger title-defect protection when permits, easements, or prior transfers need clean validation."
        },
        landlord: {
          title: "Dwelling fire conversion option",
          fit: "Optional fallback",
          premium: "$44/mo add-on est.",
          summary: "Useful when the property may become an interim rental during relocation timing changes."
        },
        life: {
          title: "Family term life + mortgage rider",
          fit: "Recommended for dependents",
          premium: "$61/mo est.",
          summary: "Pairs beneficiary protection with mortgage continuity for family relocation scenarios."
        }
      }
    }
  },
  investor: {
    profileLabel: "Income and landlord operator",
    secureExchange: "ACORD 83 dwelling property / ACORD 101 underwriting data transfer",
    controls: [
      "NAIC-aligned service-provider oversight, breach escalation, and role-based quote access are enforced for partner workflows.",
      "Tenant occupancy, peril, and prior-loss details are shared only under purpose-bound underwriting scopes.",
      "Outbound quote packets require encryption in transit, carrier authorization checks, and audit-ready retransmission controls."
    ],
    options: {
      multifamily: {
        homeowners: {
          title: "Limited habitational property package",
          fit: "Secondary recommendation",
          premium: "$228/mo est.",
          summary: "A habitational property package can cover common areas or mixed-use owner occupancy, but landlord cover is usually primary."
        },
        titlePolicy: {
          title: "Lender + owner title stack",
          fit: "Required for debt-backed closing",
          premium: "$3,480 one-time est.",
          summary: "Supports clean transfer, lender protection, and post-close claim defense for encumbrance or survey defects."
        },
        landlord: {
          title: "Landlord package + loss-of-rents + umbrella",
          fit: "Primary recommendation",
          premium: "$322/mo est.",
          summary: "Best fit for rental assets because it combines property, premises liability, rent interruption, and catastrophe endorsements."
        },
        life: {
          title: "Key-person / debt continuity life cover",
          fit: "Recommended for guarantors",
          premium: "$74/mo est.",
          summary: "Reduces execution risk when lender covenants or family office structures depend on a principal earner or guarantor."
        }
      },
      townhouse: {
        homeowners: {
          title: "DP-3 dwelling package",
          fit: "Primary recommendation for single-rental stock",
          premium: "$214/mo est.",
          summary: "Covers dwelling risks, liability, and fair-rental-value loss for smaller landlord holdings."
        },
        titlePolicy: {
          title: "Owner's title insurance",
          fit: "Recommended at acquisition",
          premium: "$2,640 one-time est.",
          summary: "Keeps transfer defects and lien surprises from impairing yield or refinancing plans."
        },
        landlord: {
          title: "Landlord liability + rent default add-on",
          fit: "Primary recommendation",
          premium: "$296/mo est.",
          summary: "Pairs rent interruption, premises liability, and optional legal expense protection for active rental operators."
        },
        life: {
          title: "Term life for debt-service continuity",
          fit: "Recommended when leverage is used",
          premium: "$58/mo est.",
          summary: "Useful for investors with financing exposure or family reliance on portfolio cashflows."
        }
      }
    }
  },
  advisor: {
    profileLabel: "Suitability-led advisory coverage review",
    secureExchange: "ACORD summary packet with title, property, and beneficiary disclosures for approval workflows",
    controls: [
      "NAIC-aligned consumer notice, access recertification, and secure disposal requirements are attached to the advisory packet.",
      "Advisor release only exposes policy classes, exclusions, and underwriting blockers that fit entitlement scope.",
      "Evidence routing preserves consent, redaction, and tamper-evident transmission controls for partner servicing teams."
    ],
    options: {
      luxury: {
        homeowners: {
          title: "High-value homeowners + valuables schedule",
          fit: "Primary recommendation",
          premium: "$352/mo est.",
          summary: "Designed for premium residences with higher contents values, broader liability expectations, and counsel-visible exclusions."
        },
        titlePolicy: {
          title: "Enhanced title with fraud defense",
          fit: "Recommended for approval-ready closing",
          premium: "$3,120 one-time est.",
          summary: "Extends title protection where premium assets need stronger fraud, recording, and ownership challenge defenses."
        },
        landlord: {
          title: "Executive landlord contingency cover",
          fit: "Optional if client may lease later",
          premium: "$64/mo add-on est.",
          summary: "Useful when premium residences may shift into limited rental use after client relocation or portfolio changes."
        },
        life: {
          title: "High-limit term life + estate liquidity rider",
          fit: "Recommended for family-office cases",
          premium: "$96/mo est.",
          summary: "Supports payment continuity, estate planning, and beneficiary protection for complex ownership structures."
        }
      },
      condo: {
        homeowners: {
          title: "HO-6 plus liability and legal expense",
          fit: "Primary recommendation",
          premium: "$198/mo est.",
          summary: "Fits premium advisory cases where internal finishes, contents, and association gap risk need explicit coverage."
        },
        titlePolicy: {
          title: "Owner's title policy",
          fit: "Recommended",
          premium: "$2,040 one-time est.",
          summary: "Provides strong closing defense without the broader cost profile of enhanced luxury title packages."
        },
        landlord: {
          title: "Short-term lease endorsement",
          fit: "Optional",
          premium: "$42/mo add-on est.",
          summary: "Adds controlled rental flexibility while preserving advisory clarity on exclusions and servicing limits."
        },
        life: {
          title: "Term life / family protection",
          fit: "Recommended when dependents rely on household income",
          premium: "$55/mo est.",
          summary: "Aligns payment continuity with family or beneficiary needs where leverage or relocation expenses are material."
        }
      }
    }
  }
};

const paymentProfiles = {
  buyer: {
    label: "Earnest money and closing funding",
    tokenization: "Hosted card/bank fields with PSP token vault",
    controls: [
      "PCI DSS segmented payment page with hosted fields and no raw PAN storage in the EstateOS frontend.",
      "Velocity, device, geo, and beneficiary checks are evaluated before escrow release is marked ready.",
      "Authorizations, captures, and escrow ledger movements reconcile against immutable settlement references."
    ]
  },
  investor: {
    label: "Cross-border capital movement and escrow",
    tokenization: "Tokenized ACH/wire orchestration with bank-account aliasing",
    controls: [
      "Cross-border funding is screened for payer-behavior anomalies, sanctions adjacency, and settlement delays.",
      "Escrow release requires source-of-funds confirmation, beneficiary matching, and exception-free reconciliation state.",
      "Operations analysts receive manual review queues when fraud probability, amount, or geography exceeds threshold."
    ]
  },
  advisor: {
    label: "Approval-controlled disbursement oversight",
    tokenization: "Advisor console uses PSP-hosted confirmation views and masked settlement references",
    controls: [
      "Segregation of duties is enforced between recommendation approval, payment release, and reconciliation closeout.",
      "Manual review evidence, override rationale, and release approvals are linked to the immutable transaction ledger.",
      "PCI DSS, ISO/IEC 27001, and ISO 22301 controls protect release actions, recovery steps, and settlement traceability."
    ]
  }
};

const integrationProfiles = {
  banking_core: {
    label: "Banking core settlement adapter",
    summary: "Banking messages are normalized into a canonical funds-movement contract before finance, payment-risk, and compliance experts approve downstream settlement or escrow actions.",
    canonicalModel: "CanonicalPaymentInstruction v1",
    expertChain: ["Payment intelligence", "Finance", "Compliance"],
    security: "mTLS • field encryption • token vault aliasing",
    routeTarget: "Escrow and settlement orchestration",
    controls: [
      { title: "Schema and balance validation", status: "Pass", detail: "The adapter verifies account alias references, amount tolerances, settlement windows, and beneficiary fields before the payload is accepted." },
      { title: "Expert transformation", status: "Active", detail: "Finance and payment experts enrich ISO 20022, ACH, or PSP payloads into the EstateOS canonical contract with traceable field mappings." },
      { title: "Release gate", status: "Policy enforced", detail: "Fraud score, sanctions posture, entitlements, and dual approval state are checked before the instruction reaches escrow release workflows." }
    ],
    routes: [
      { title: "Primary route", status: "Escrow orchestration", detail: "Approved instructions feed the payment risk service, escrow ledger, and reconciliation engine with the same correlation ID." },
      { title: "Fallback route", status: "Manual review queue", detail: "Out-of-policy amounts or unsettled funding paths move into analyst review without breaking the evidence chain." }
    ],
    evidence: [
      { title: "Interoperability record", status: "ISO 20022 + NACHA mapping", detail: "Canonical field lineage captures how external banking fields were transformed for internal use." },
      { title: "Compliance record", status: "PCI DSS + AML/KYC", detail: "Token references, sanctions checks, and settlement approvals are retained in the audit ledger." }
    ]
  },
  insurance_exchange: {
    label: "Carrier and broker exchange adapter",
    summary: "Carrier connectivity uses ACORD-style canonical payloads so underwriting, exposure, and policy recommendations can be validated by insurance and compliance experts before any quote request is routed externally.",
    canonicalModel: "CanonicalCoverageExchange v1",
    expertChain: ["Insurance", "Risk", "Compliance"],
    security: "mTLS • signed envelopes • redaction policy",
    routeTarget: "Quote matching and underwriting intake",
    controls: [
      { title: "Coverage payload validation", status: "Pass", detail: "ACORD-aligned dwelling, occupancy, peril, and applicant fields are checked against canonical schema and consent scope." },
      { title: "Expert augmentation", status: "Active", detail: "Insurance and risk experts add hazard, underwriting readiness, and policy-fit metadata before partner delivery." },
      { title: "Privacy boundary", status: "Purpose bound", detail: "Only role-approved fields are released to brokers or carriers, with NAIC-aligned sharing and retention controls." }
    ],
    routes: [
      { title: "Primary route", status: "Carrier marketplace", detail: "Release-ready requests flow to the insurer workspace and partner APIs with quote correlation and evidence references." },
      { title: "Fallback route", status: "Advisory escalation", detail: "Complex or surplus-lines cases route to an advisor desk with the same normalized payload and control trace." }
    ],
    evidence: [
      { title: "Interoperability record", status: "ACORD mapping", detail: "Coverage, party, and loss-history fields keep a canonical-to-partner mapping ledger for downstream audits." },
      { title: "Compliance record", status: "NAIC + ISO/IEC 27701", detail: "Consent receipts, field-level redaction choices, and partner release decisions are preserved." }
    ]
  },
  government_registry: {
    label: "Government registry and residency adapter",
    summary: "Government and registry interfaces normalize property, identity, and filing data so residency, document, and compliance experts can validate submissions before routing them to public-sector systems.",
    canonicalModel: "CanonicalJurisdictionSubmission v1",
    expertChain: ["Residency", "Document QA", "Compliance"],
    security: "private endpoints • signed submissions • jurisdiction vaulting",
    routeTarget: "Residency filing and land-registry submission",
    controls: [
      { title: "Jurisdiction rule validation", status: "Pass", detail: "The adapter checks local filing versions, mandatory supporting documents, and residency-specific business rules before submission." },
      { title: "Expert transformation", status: "Active", detail: "Residency and document experts translate user-facing evidence into jurisdiction-specific filing packages with explainable exception flags." },
      { title: "Cross-border compliance", status: "Policy enforced", detail: "Data residency, source-of-funds, sanctions, and retention rules determine whether the payload can be released or must be held." }
    ],
    routes: [
      { title: "Primary route", status: "Public-sector connector", detail: "Eligible payloads route through API Management to registry, visa, or municipal APIs with signed service identities." },
      { title: "Fallback route", status: "Counsel review", detail: "Jurisdiction mismatches or missing evidence pause submission and send a guided remediation package to legal or migration teams." }
    ],
    evidence: [
      { title: "Interoperability record", status: "Schema version ledger", detail: "Each submission stores the jurisdiction contract version, transformed fields, and exception notes used at release time." },
      { title: "Compliance record", status: "ISO/IEC 27001 + 27701", detail: "Consent scope, cross-border transfer controls, and manual sign-off records remain attached to the filing event." }
    ]
  }
};

const governanceProfiles = [
  {
    framework: "ISO/IEC 27001",
    title: "Information security governance",
    summary: "Access segregation, MFA, immutable evidence, and security monitoring protect sensitive deal and recommendation workflows.",
    controls: "RBAC • MFA • Evidence retention • Security monitoring"
  },
  {
    framework: "ISO 22301",
    title: "Business continuity governance",
    summary: "Transaction workflows use replayable stage events, alternate queues, and recovery checkpoints to preserve continuity.",
    controls: "RTO/RPO checkpoints • Workflow replay • Alternate queue • Manual runbook"
  },
  {
    framework: "ISO/IEC 42001",
    title: "AI management governance",
    summary: "Valuation, recommendation, pricing, and risk models are managed with accountable ownership, explainability, and human oversight triggers.",
    controls: "Model inventory • Human review • Fairness checks • Explanation ledger"
  }
];

const state = {
  activeJourney: "buyer",
  objective: "relocate",
  risk: "balanced",
  explanationDepth: "guided",
  budget: 650000,
  residency: true,
  financing: true,
  jurisdiction: "Portugal",
  annualIncome: 145000,
  liquidAssets: 280000,
  propertyValue: 620000,
  sourceOfFundsVerified: true,
  criminalRecordClear: true,
  healthInsuranceReady: true,
  insurancePropertyType: "single_family",
  insuranceTransactionContext: "purchase",
  insuranceOccupancy: "owner_occupied",
  insuranceHouseholdRisk: "family_protection",
  insuranceNeedsTitle: true,
  insuranceNeedsLandlord: false,
  insuranceNeedsLife: true,
  paymentMethod: "bank_transfer",
  paymentEscrowStage: "deposit_pending",
  paymentAmount: 25000,
  paymentSettlementTiming: "same_day",
  paymentTrustedDevice: true,
  paymentCrossBorder: false,
  paymentManualReview: false,
  integrationPartner: "banking_core"
};

const title = document.getElementById("journey-title");
const summary = document.getElementById("journey-summary");
const confidence = document.getElementById("journey-confidence");
const releaseStatus = document.getElementById("release-status");
const headline = document.getElementById("recommendation-headline");
const subtitle = document.getElementById("recommendation-subtitle");
const steps = document.getElementById("journey-steps");
const action = document.getElementById("journey-action");
const risk = document.getElementById("journey-risk");
const why = document.getElementById("journey-why");
const expertStrip = document.getElementById("expert-strip");
const journeyButtons = document.querySelectorAll(".journey-card");
const investorType = document.getElementById("profile-investor-type");
const locationValue = document.getElementById("profile-location");
const financialIntent = document.getElementById("profile-financial-intent");
const residencyGoal = document.getElementById("profile-residency-goal");
const accessState = document.getElementById("profile-access-state");
const personaSelect = document.getElementById("persona-select");
const objectiveSelect = document.getElementById("objective-select");
const riskSelect = document.getElementById("risk-select");
const explanationSelect = document.getElementById("explanation-select");
const budgetRange = document.getElementById("budget-range");
const budgetValue = document.getElementById("budget-value");
const residencyToggle = document.getElementById("residency-toggle");
const financingToggle = document.getElementById("financing-toggle");
const propertyList = document.getElementById("property-list");
const insightList = document.getElementById("insight-list");
const visaList = document.getElementById("visa-list");
const insuranceList = document.getElementById("insurance-list");
const valuationList = document.getElementById("valuation-list");
const governanceList = document.getElementById("governance-list");
const contributionList = document.getElementById("contribution-list");
const nextActionsList = document.getElementById("next-actions");
const propertyFitPill = document.getElementById("property-fit-pill");
const dealTitle = document.getElementById("deal-title");
const dealSummary = document.getElementById("deal-summary");
const dealRiskPill = document.getElementById("deal-risk-pill");
const dealTargetPrice = document.getElementById("deal-target-price");
const dealCloseWindow = document.getElementById("deal-close-window");
const dealIntegrity = document.getElementById("deal-integrity");
const dealContinuity = document.getElementById("deal-continuity");
const dealStageList = document.getElementById("deal-stage-list");
const dealExpertList = document.getElementById("deal-expert-list");
const documentList = document.getElementById("document-list");
const complianceControlList = document.getElementById("compliance-control-list");
const jurisdictionSelect = document.getElementById("jurisdiction-select");
const incomeRange = document.getElementById("income-range");
const incomeValue = document.getElementById("income-value");
const assetsRange = document.getElementById("assets-range");
const assetsValue = document.getElementById("assets-value");
const propertyValueRange = document.getElementById("property-value-range");
const propertyValueLabel = document.getElementById("property-value");
const sourceOfFundsToggle = document.getElementById("source-of-funds-toggle");
const criminalRecordToggle = document.getElementById("criminal-record-toggle");
const healthInsuranceToggle = document.getElementById("health-insurance-toggle");
const residencyProgramTitle = document.getElementById("residency-program-title");
const residencyStatusPill = document.getElementById("residency-status-pill");
const residencySummary = document.getElementById("residency-summary");
const eligibilityScore = document.getElementById("eligibility-score");
const pathwayType = document.getElementById("pathway-type");
const kycAmlSummary = document.getElementById("kyc-aml-summary");
const privacySummary = document.getElementById("privacy-summary");
const ruleCheckList = document.getElementById("rule-check-list");
const documentCheckList = document.getElementById("document-check-list");
const complianceWorkflowList = document.getElementById("compliance-workflow-list");
const insuranceProgramTitle = document.getElementById("insurance-program-title");
const insuranceStatusPill = document.getElementById("insurance-status-pill");
const insuranceSummary = document.getElementById("insurance-summary");
const insurancePropertyType = document.getElementById("insurance-property-type");
const insuranceTransactionContext = document.getElementById("insurance-transaction-context");
const insuranceOccupancy = document.getElementById("insurance-occupancy");
const insuranceHouseholdRisk = document.getElementById("insurance-household-risk");
const insuranceTitleToggle = document.getElementById("insurance-title-toggle");
const insuranceLandlordToggle = document.getElementById("insurance-landlord-toggle");
const insuranceLifeToggle = document.getElementById("insurance-life-toggle");
const insuranceReadinessScore = document.getElementById("insurance-readiness-score");
const insurancePrimaryPackage = document.getElementById("insurance-primary-package");
const insuranceAcordMode = document.getElementById("insurance-acord-mode");
const insuranceNaicPosture = document.getElementById("insurance-naic-posture");
const insuranceOptionList = document.getElementById("insurance-option-list");
const insurancePayloadList = document.getElementById("insurance-payload-list");
const insuranceControlList = document.getElementById("insurance-control-list");
const paymentProgramTitle = document.getElementById("payment-program-title");
const paymentStatusPill = document.getElementById("payment-status-pill");
const paymentSummary = document.getElementById("payment-summary");
const paymentMethodSelect = document.getElementById("payment-method-select");
const paymentEscrowStage = document.getElementById("payment-escrow-stage");
const paymentAmountRange = document.getElementById("payment-amount-range");
const paymentAmountValue = document.getElementById("payment-amount-value");
const paymentSettlementSelect = document.getElementById("payment-settlement-select");
const paymentDeviceTrusted = document.getElementById("payment-device-trusted");
const paymentCrossBorder = document.getElementById("payment-cross-border");
const paymentManualReview = document.getElementById("payment-manual-review");
const paymentFraudScore = document.getElementById("payment-fraud-score");
const paymentBehaviorSummary = document.getElementById("payment-behavior-summary");
const paymentEscrowSummary = document.getElementById("payment-escrow-summary");
const paymentFrontendPosture = document.getElementById("payment-frontend-posture");
const paymentSignalList = document.getElementById("payment-signal-list");
const paymentEscrowList = document.getElementById("payment-escrow-list");
const paymentReconciliationList = document.getElementById("payment-reconciliation-list");
const integrationProgramTitle = document.getElementById("integration-program-title");
const integrationStatusPill = document.getElementById("integration-status-pill");
const integrationSummary = document.getElementById("integration-summary");
const integrationPartnerSelect = document.getElementById("integration-partner-select");
const integrationCanonicalModel = document.getElementById("integration-canonical-model");
const integrationExpertChain = document.getElementById("integration-expert-chain");
const integrationSecurityPosture = document.getElementById("integration-security-posture");
const integrationRouteTarget = document.getElementById("integration-route-target");
const integrationControlList = document.getElementById("integration-control-list");
const integrationRouteList = document.getElementById("integration-route-list");
const integrationEvidenceList = document.getElementById("integration-evidence-list");

function currency(value) {
  return new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    maximumFractionDigits: 0
  }).format(value);
}

function populateStaticControls() {
  personaSelect.innerHTML = Object.entries(journeys)
    .map(([key, journey]) => `<option value="${key}">${journey.title}</option>`)
    .join("");

  jurisdictionSelect.innerHTML = Object.keys(residencyPrograms)
    .map((jurisdiction) => `<option value="${jurisdiction}">${jurisdiction}</option>`)
    .join("");

  riskSelect.innerHTML = [
    ["conservative", "Conservative"],
    ["balanced", "Balanced"],
    ["opportunistic", "Opportunistic"]
  ]
    .map(([value, label]) => `<option value="${value}">${label}</option>`)
    .join("");

  explanationSelect.innerHTML = [
    ["guided", "Guided"],
    ["detailed", "Detailed"],
    ["full", "Full evidence"]
  ]
    .map(([value, label]) => `<option value="${value}">${label}</option>`)
    .join("");

  insurancePropertyType.innerHTML = [
    ["single_family", "Single-family home"],
    ["condo", "Condo / apartment"],
    ["townhouse", "Townhouse"],
    ["multifamily", "Multifamily / rental block"],
    ["luxury", "Luxury residence"]
  ]
    .map(([value, label]) => `<option value="${value}">${label}</option>`)
    .join("");

  insuranceTransactionContext.innerHTML = [
    ["purchase", "Purchase / offer stage"],
    ["closing", "Closing and title binding"],
    ["refinance", "Refinance / restructure"],
    ["portfolio", "Portfolio review"]
  ]
    .map(([value, label]) => `<option value="${value}">${label}</option>`)
    .join("");

  insuranceOccupancy.innerHTML = [
    ["owner_occupied", "Owner occupied"],
    ["second_home", "Second home"],
    ["tenant_occupied", "Tenant occupied"],
    ["mixed_use", "Mixed use / flexible"]
  ]
    .map(([value, label]) => `<option value="${value}">${label}</option>`)
    .join("");

  insuranceHouseholdRisk.innerHTML = [
    ["family_protection", "Family protection"],
    ["asset_preservation", "Asset preservation"],
    ["debt_continuity", "Debt continuity"],
    ["estate_planning", "Estate planning"]
  ]
    .map(([value, label]) => `<option value="${value}">${label}</option>`)
    .join("");

  paymentMethodSelect.innerHTML = [
    ["bank_transfer", "Bank transfer / ACH"],
    ["card_token", "Card on file token"],
    ["wire", "Domestic / SWIFT wire"],
    ["wallet", "Digital wallet"],
    ["escrow_disbursement", "Escrow disbursement"]
  ]
    .map(([value, label]) => `<option value="${value}">${label}</option>`)
    .join("");

  paymentEscrowStage.innerHTML = [
    ["deposit_pending", "Deposit pending"],
    ["funds_received", "Funds received"],
    ["docs_cleared", "Documents cleared"],
    ["release_pending", "Release pending"],
    ["disbursed", "Disbursed"]
  ]
    .map(([value, label]) => `<option value="${value}">${label}</option>`)
    .join("");

  paymentSettlementSelect.innerHTML = [
    ["same_day", "Same day"],
    ["next_day", "Next business day"],
    ["scheduled", "Scheduled batch"],
    ["manual_hold", "Manual hold / review"]
  ]
    .map(([value, label]) => `<option value="${value}">${label}</option>`)
    .join("");


  integrationPartnerSelect.innerHTML = Object.entries(integrationProfiles)
    .map(([value, profile]) => `<option value="${value}">${profile.label}</option>`)
    .join("");
}

function applyJourneyDefaults(journeyKey) {
  const journey = journeys[journeyKey];
  state.activeJourney = journeyKey;
  state.objective = journey.defaults.objective;
  state.risk = journey.defaults.risk;
  state.explanationDepth = journey.defaults.explanationDepth;
  state.budget = journey.defaults.budget;
  state.residency = journey.defaults.residency;
  state.financing = journey.defaults.financing;

  personaSelect.value = journeyKey;
  riskSelect.value = state.risk;
  explanationSelect.value = state.explanationDepth;
  budgetRange.value = state.budget;
  residencyToggle.checked = state.residency;
  financingToggle.checked = state.financing;
  state.jurisdiction = journeyKey === "investor" ? "Greece" : journeyKey === "advisor" ? "UAE" : "Portugal";
  state.propertyValue = Math.min(Math.max(journey.candidates[0].price, 0), Number(propertyValueRange.max || 2000000));
  jurisdictionSelect.value = state.jurisdiction;
  incomeRange.value = state.annualIncome;
  assetsRange.value = state.liquidAssets;
  propertyValueRange.value = state.propertyValue;
  sourceOfFundsToggle.checked = state.sourceOfFundsVerified;
  criminalRecordToggle.checked = state.criminalRecordClear;
  healthInsuranceToggle.checked = state.healthInsuranceReady;
  state.insurancePropertyType = journeyKey === "investor" ? "multifamily" : journeyKey === "advisor" ? "luxury" : "single_family";
  state.insuranceTransactionContext = journeyKey === "advisor" ? "closing" : "purchase";
  state.insuranceOccupancy = journeyKey === "investor" ? "tenant_occupied" : "owner_occupied";
  state.insuranceHouseholdRisk = journeyKey === "investor" ? "asset_preservation" : journeyKey === "advisor" ? "estate_planning" : "family_protection";
  state.insuranceNeedsTitle = true;
  state.insuranceNeedsLandlord = journeyKey === "investor";
  state.insuranceNeedsLife = journeyKey !== "investor" || state.financing;
  insurancePropertyType.value = state.insurancePropertyType;
  insuranceTransactionContext.value = state.insuranceTransactionContext;
  insuranceOccupancy.value = state.insuranceOccupancy;
  insuranceHouseholdRisk.value = state.insuranceHouseholdRisk;
  insuranceTitleToggle.checked = state.insuranceNeedsTitle;
  insuranceLandlordToggle.checked = state.insuranceNeedsLandlord;
  insuranceLifeToggle.checked = state.insuranceNeedsLife;
  state.paymentMethod = journeyKey === "buyer" ? "bank_transfer" : journeyKey === "advisor" ? "escrow_disbursement" : "wire";
  state.paymentEscrowStage = journeyKey === "advisor" ? "release_pending" : journeyKey === "investor" ? "funds_received" : "deposit_pending";
  state.paymentAmount = journeyKey === "buyer" ? 25000 : journeyKey === "advisor" ? 85000 : 120000;
  state.paymentSettlementTiming = journeyKey === "buyer" ? "same_day" : journeyKey === "advisor" ? "manual_hold" : "next_day";
  state.paymentTrustedDevice = true;
  state.paymentCrossBorder = journeyKey !== "buyer";
  state.paymentManualReview = journeyKey === "advisor";
  state.integrationPartner = journeyKey === "buyer" ? "banking_core" : journeyKey === "investor" ? "government_registry" : "insurance_exchange";
  paymentMethodSelect.value = state.paymentMethod;
  paymentEscrowStage.value = state.paymentEscrowStage;
  paymentAmountRange.value = state.paymentAmount;
  paymentSettlementSelect.value = state.paymentSettlementTiming;
  paymentDeviceTrusted.checked = state.paymentTrustedDevice;
  paymentCrossBorder.checked = state.paymentCrossBorder;
  paymentManualReview.checked = state.paymentManualReview;
  integrationPartnerSelect.value = state.integrationPartner;
  populateObjectives();
  objectiveSelect.value = state.objective;
}

function populateObjectives() {
  const options = journeys[state.activeJourney].objectives;
  objectiveSelect.innerHTML = options.map((option) => `<option value="${option.value}">${option.label}</option>`).join("");
}

function getIntelligence(candidate) {
  return propertyIntelligence[candidate.id];
}

function getRecommendationScore(candidate) {
  const intelligence = getIntelligence(candidate);
  const baseScore = intelligence ? 0.88 : 0.8;
  const fitScore = (candidate.experts.property + candidate.experts.finance + candidate.experts.compliance) / 3;
  return Number(((baseScore + fitScore) / 2).toFixed(2));
}

function buildWeights() {
  const base = { property: 0.18, investment: 0.16, visa: 0.12, insurance: 0.12, finance: 0.14, compliance: 0.12, recommendation: 0.16 };
  const { activeJourney, objective, risk: riskMode, residency, financing, explanationDepth } = state;

  if (activeJourney === "buyer") {
    base.property += 0.08;
    base.finance += 0.05;
    base.recommendation += 0.07;
  }
  if (activeJourney === "investor") {
    base.investment += 0.1;
    base.property += 0.04;
    base.recommendation += 0.05;
  }
  if (activeJourney === "advisor") {
    base.compliance += 0.1;
    base.finance += 0.04;
    base.recommendation += 0.04;
  }

  if (objective === "yield") base.investment += 0.08;
  if (objective === "yield") base.recommendation += 0.03;
  if (objective === "diversify") base.property += 0.04;
  if (objective === "diversify") base.recommendation += 0.03;
  if (objective === "residency" || objective === "relocate") base.visa += 0.08;
  if (objective === "residency" || objective === "relocate") base.recommendation += 0.03;
  if (objective === "stability" || objective === "suitability") base.compliance += 0.06;
  if (objective === "stability" || objective === "suitability") base.recommendation += 0.02;
  if (objective === "lifestyle") base.property += 0.06;
  if (objective === "lifestyle") base.recommendation += 0.03;
  if (objective === "approval" || objective === "evidence") base.compliance += 0.05;
  if (objective === "approval" || objective === "evidence") base.recommendation += 0.03;

  if (riskMode === "conservative") {
    base.compliance += 0.05;
    base.insurance += 0.04;
    base.finance += 0.03;
    base.recommendation += 0.02;
  }
  if (riskMode === "opportunistic") {
    base.investment += 0.05;
    base.property += 0.03;
    base.recommendation += 0.03;
  }

  if (residency) {
    base.visa += 0.06;
    base.recommendation += 0.02;
  }
  if (financing) base.finance += 0.06;
  else {
    base.investment += 0.02;
    base.recommendation += 0.02;
  }

  if (explanationDepth === "full") {
    base.compliance += 0.02;
    base.recommendation += 0.02;
  }

  const total = Object.values(base).reduce((sum, value) => sum + value, 0);
  return Object.fromEntries(Object.entries(base).map(([key, value]) => [key, value / total]));
}

function scoreCandidate(candidate) {
  const weights = buildWeights();
  const budgetRatio = Math.max(0, Math.min(1, state.budget / candidate.price));
  const budgetBoost = candidate.price <= state.budget ? 0.06 : -0.07 * (1 - budgetRatio);
  const residencyBoost = state.residency ? candidate.experts.visa * 0.05 : 0;
  const financingBoost = state.financing ? candidate.financingFit * 0.05 : 0;
  const climatePenalty =
    state.risk === "conservative" && candidate.climateRisk === "medium"
      ? 0.035
      : state.risk === "conservative" && candidate.climateRisk === "high"
        ? 0.07
        : 0;

  const enrichedExperts = { ...candidate.experts, recommendation: getRecommendationScore(candidate) };
  const weightedScore = Object.entries(enrichedExperts).reduce((sum, [expert, expertScore]) => sum + expertScore * weights[expert], 0);

  return Number((weightedScore + budgetBoost + residencyBoost + financingBoost - climatePenalty).toFixed(3));
}

function rankCandidates() {
  return journeys[state.activeJourney].candidates
    .map((candidate) => ({ ...candidate, aggregateScore: scoreCandidate(candidate) }))
    .sort((a, b) => b.aggregateScore - a.aggregateScore);
}

function getReleaseTone() {
  if (state.activeJourney === "advisor") return "Approval-ready";
  if (state.activeJourney === "investor") return state.risk === "opportunistic" ? "Reviewable with advisor" : "Ready with review";
  return "Ready to release";
}

function buildWhyText(topCandidate) {
  const weights = buildWeights();
  const sortedContributors = Object.entries({ ...topCandidate.experts, recommendation: getRecommendationScore(topCandidate) })
    .map(([key, value]) => ({ key, value, weighted: value * weights[key] }))
    .sort((a, b) => b.weighted - a.weighted)
    .slice(0, 3)
    .map((item) => expertMeta[item.key].label.toLowerCase());

  if (state.explanationDepth === "guided") {
    return `${topCandidate.title} leads because ${sortedContributors.join(", ")} align best with the current goals, budget, trust posture, and transaction stage.`;
  }

  return `${topCandidate.title} leads because the ${sortedContributors[0]} contributed most to the composite score, while budget fit, ${
    state.residency ? "residency eligibility, " : ""
  }transaction readiness, and ${state.financing ? "financing readiness" : "compliance confidence"} remained stronger than the alternatives.`;
}

function buildRiskText(topCandidate) {
  const budgetDelta = state.budget - topCandidate.price;
  const budgetText = budgetDelta >= 0 ? `within budget by ${currency(budgetDelta)}` : `above budget by ${currency(Math.abs(budgetDelta))}`;
  const intelligence = getIntelligence(topCandidate);
  const deal = journeys[state.activeJourney].deal;
  const paymentScenario = getPaymentScenario();
  return `${topCandidate.insurance.summary} ${intelligence.trend} The current recommendation is ${budgetText}, climate risk is ${topCandidate.climateRisk}, payment release posture is ${paymentScenario.status.toLowerCase()}, and the live transaction posture is ${deal.riskLabel.toLowerCase()} with ${deal.integrity.toLowerCase()} workflow integrity.`;
}

function buildActionText(topCandidate) {
  if (state.activeJourney === "advisor") {
    return `Prepare a client memo for ${topCandidate.title}, confirm policy evidence, and use the transaction ledger to justify why it outranks the rest of the shortlist.`;
  }
  if (state.activeJourney === "investor") {
    return `Advance ${topCandidate.title} into diligence, then compare downside resilience, optional residency steps, negotiation leverage, and document exceptions before capital is committed.`;
  }
  return `Prioritize ${topCandidate.title}, move into financing and residency planning, and resolve open disclosure issues before the transaction shifts into approval.`;
}

function renderPropertyList(rankedCandidates) {
  propertyList.innerHTML = rankedCandidates
    .map((candidate, index) => {
      const delta = Math.round(candidate.aggregateScore * 100);
      return `
        <article class="recommendation-item ${index === 0 ? "recommendation-item--featured" : ""}">
          <div class="recommendation-topline">
            <strong>#${index + 1} ${candidate.title}</strong>
            <span>${candidate.location}</span>
          </div>
          <p>${candidate.summary}</p>
          <div class="meta-row">
            <span>Price ${currency(candidate.price)}</span>
            <span>Score ${delta}/100</span>
            <span>Value band ${getIntelligence(candidate).valuationBand}</span>
          </div>
          <div class="tag-row">
            ${candidate.tags.map((tag) => `<span>${tag}</span>`).join("")}
          </div>
          <p class="helper-copy">${candidate.why}</p>
        </article>
      `;
    })
    .join("");
  propertyFitPill.textContent = `Top match: ${rankedCandidates[0].location}`;
}

function renderInsights(rankedCandidates) {
  insightList.innerHTML = rankedCandidates
    .slice(0, 2)
    .map(
      (candidate) => `
        <div class="stack-item">
          <strong>${candidate.title}</strong>
          <p>${candidate.insight}</p>
        </div>
      `
    )
    .join("");

  visaList.innerHTML = rankedCandidates
    .slice(0, 2)
    .map(
      (candidate) => `
        <div class="stack-item">
          <strong>${candidate.visaPathway.title}</strong>
          <span>${candidate.visaPathway.fit}</span>
          <p>${candidate.visaPathway.summary}</p>
        </div>
      `
    )
    .join("");

  insuranceList.innerHTML = rankedCandidates
    .slice(0, 2)
    .map(
      (candidate) => `
        <div class="stack-item">
          <strong>${candidate.insurance.title}</strong>
          <span>${candidate.insurance.premium}</span>
          <p>${candidate.insurance.summary}</p>
        </div>
      `
    )
    .join("");
}

function renderValuation(rankedCandidates) {
  valuationList.innerHTML = rankedCandidates
    .slice(0, 2)
    .map((candidate) => {
      const intelligence = getIntelligence(candidate);
      return `
        <div class="stack-item">
          <strong>${candidate.title} • ${intelligence.valuationBand}</strong>
          <span>${intelligence.comparables}</span>
          <p>${intelligence.trend} ${intelligence.location}</p>
        </div>
      `;
    })
    .join("");
}

function renderGovernance() {
  governanceList.innerHTML = governanceProfiles
    .map(
      (profile) => `
      <div class="stack-item">
        <strong>${profile.framework} • ${profile.title}</strong>
        <span>${profile.controls}</span>
        <p>${profile.summary}</p>
      </div>
    `
    )
    .join("");
}

function renderContributions(topCandidate) {
  const weights = buildWeights();
  const entries = Object.entries({ ...topCandidate.experts, recommendation: getRecommendationScore(topCandidate) })
    .map(([key, value]) => ({ key, value, weighted: value * weights[key] }))
    .sort((a, b) => b.weighted - a.weighted);

  contributionList.innerHTML = entries
    .map((entry) => {
      const percent = Math.round(entry.weighted * 100);
      const raw = Math.round(entry.value * 100);
      const detail =
        state.explanationDepth === "guided"
          ? `${expertMeta[entry.key].label} supported the recommendation with a ${raw}/100 signal.`
          : `${expertMeta[entry.key].label} contributed ${percent} weighted points from a raw ${raw}/100 score after persona, objective, and trust adjustments.`;
      return `
        <div class="stack-item contribution-item">
          <div class="contribution-header">
            <strong>${expertMeta[entry.key].label}</strong>
            <span>${percent} weighted pts</span>
          </div>
          <div class="progress-track"><span style="width:${Math.max(percent, 8)}%"></span></div>
          <p>${detail}</p>
        </div>
      `;
    })
    .join("");
}

function renderDealBoard() {
  const deal = journeys[state.activeJourney].deal;
  dealTitle.textContent = deal.name;
  dealSummary.textContent = deal.summary;
  dealRiskPill.textContent = deal.riskLabel;
  dealTargetPrice.textContent = currency(deal.targetPrice);
  dealCloseWindow.textContent = deal.closeWindow;
  dealIntegrity.textContent = deal.integrity;
  dealContinuity.textContent = deal.continuityMode;

  dealStageList.innerHTML = deal.stages
    .map(
      (stage) => `
        <div class="stage-item stage-item--${stage.status.replace(/\s+/g, "-")}">
          <div class="stage-heading">
            <strong>${stage.stage}</strong>
            <span>${stage.status}</span>
          </div>
          <div class="progress-track"><span style="width:${stage.progress}%"></span></div>
          <p>${stage.note}</p>
          <small>Owner • ${stage.owner}</small>
        </div>
      `
    )
    .join("");

  dealExpertList.innerHTML = deal.experts
    .map(
      (item) => `
        <div class="stack-item">
          <div class="recommendation-topline">
            <strong>${item.title}</strong>
            <span>${item.status} • ${Math.round(item.score * 100)}/100</span>
          </div>
          <p>${item.summary}</p>
        </div>
      `
    )
    .join("");

  documentList.innerHTML = deal.documents
    .map(
      (document) => `
        <div class="stack-item">
          <div class="recommendation-topline">
            <strong>${document.name}</strong>
            <span>${document.status}</span>
          </div>
          <p>${document.note}</p>
          <small>Owner • ${document.owner}</small>
        </div>
      `
    )
    .join("");

  complianceControlList.innerHTML = deal.controls
    .map(
      (control) => `
        <div class="stack-item">
          <div class="recommendation-topline">
            <strong>${control.control}</strong>
            <span>${control.status}</span>
          </div>
          <p>${control.detail}</p>
        </div>
      `
    )
    .join("");
}

function evaluateResidencyProgram() {
  const program = residencyPrograms[state.jurisdiction];
  const requiredDocsOnFile = [
    state.sourceOfFundsVerified ? program.documents[2] || "Proof of funds" : null,
    state.healthInsuranceReady ? "Health insurance" : null,
    state.criminalRecordClear ? "Criminal record" : null
  ].filter(Boolean);

  const ruleChecks = [
    {
      name: "Property threshold",
      status: state.propertyValue >= program.minimumPropertyValue ? "Pass" : "Review",
      detail: program.minimumPropertyValue
        ? `Property value ${currency(state.propertyValue)} vs. minimum ${currency(program.minimumPropertyValue)}.`
        : "No minimum property purchase is required for the base pathway."
    },
    {
      name: "Income threshold",
      status: state.annualIncome >= program.minimumAnnualIncome ? "Pass" : "Review",
      detail: `Annual income ${currency(state.annualIncome)} vs. minimum ${currency(program.minimumAnnualIncome)}.`
    },
    {
      name: "Liquid asset threshold",
      status: state.liquidAssets >= program.minimumLiquidAssets ? "Pass" : "Review",
      detail: `Liquid assets ${currency(state.liquidAssets)} vs. minimum ${currency(program.minimumLiquidAssets)}.`
    },
    {
      name: "Source-of-funds check",
      status: state.sourceOfFundsVerified ? "Pass" : "Review",
      detail: "KYC/AML workflow requires source-of-funds evidence before the case can be released externally."
    },
    {
      name: "Criminal record check",
      status: state.criminalRecordClear ? "Pass" : "Block",
      detail: "Jurisdiction filing remains blocked until criminal record clearance is on file."
    },
    {
      name: "Health insurance check",
      status: state.healthInsuranceReady ? "Pass" : "Review",
      detail: "Coverage confirmation is tracked because filing packets often require proof of insurance."
    }
  ];

  const documentChecks = [
    ...program.documents.map((document) => ({
      document,
      status:
        document === "Health insurance"
          ? state.healthInsuranceReady
            ? "Ready"
            : "Missing"
          : document === "Criminal record"
            ? state.criminalRecordClear
              ? "Ready"
              : "Missing"
            : document === "Proof of funds" || document === "Bank statements" || document === "Proof of income"
              ? state.sourceOfFundsVerified
                ? "Ready"
                : "Missing"
              : "Ready",
      detail: requiredDocsOnFile.includes(document) || !["Health insurance", "Criminal record", "Proof of funds", "Bank statements", "Proof of income"].includes(document)
        ? "Document is in the controlled evidence bundle or modeled as available."
        : "Document needs collection or refresh before submission."
    })),
    ...program.reviewDocuments.map((document) => ({
      document,
      status: "Recommended",
      detail: "Supplemental evidence improves legal review, family processing, or property traceability."
    }))
  ];

  const workflow = program.workflow.map((step, index) => {
    const lower = step.toLowerCase();
    const status = lower.includes("kyc")
      ? "Completed"
      : lower.includes("aml")
        ? state.sourceOfFundsVerified
          ? "Completed"
          : "Review"
        : lower.includes("privacy")
          ? "Completed"
          : lower.includes("filing") || lower.includes("sign-off")
            ? documentChecks.some((item) => item.status === "Missing")
              ? "Blocked"
              : "Ready"
            : state.propertyValue >= program.minimumPropertyValue
              ? "Ready"
              : "Review";

    return {
      step: `${index + 1}. ${step}`,
      owner: lower.includes("privacy") ? "Privacy office" : lower.includes("aml") ? "AML analyst" : lower.includes("kyc") ? "Compliance ops" : lower.includes("filing") || lower.includes("sign-off") ? "Jurisdiction counsel" : "Residency operations",
      status,
      detail: "Workflow is tracked with KYC/AML evidence, document review states, and ISO/IEC 27701 privacy controls."
    };
  });

  const blocked = ruleChecks.some((item) => item.status === "Block");
  const reviewCount = ruleChecks.filter((item) => item.status === "Review").length + documentChecks.filter((item) => item.status === "Missing").length;
  const status = blocked ? "Ineligible" : reviewCount ? "Eligible with review" : "Eligible";
  const score = Math.max(0.48, Math.min(0.99, 0.58 + ruleChecks.filter((item) => item.status === "Pass").length * 0.06 - reviewCount * 0.04 - (blocked ? 0.18 : 0)));

  return {
    program,
    status,
    score,
    ruleChecks,
    documentChecks,
    workflow,
    kycAml: state.sourceOfFundsVerified
      ? "KYC complete • AML source-of-funds matched"
      : "KYC complete • AML source-of-funds pending",
    privacy: "ISO/IEC 27701 purpose limitation • consent-scoped sharing • retention-aware evidence handling",
    summary: `${program.program} evaluates income, liquid assets, property value, and document readiness before routing cases into counsel and compliance review. ${program.notes}`
  };
}

function renderResidencyEngine() {
  const result = evaluateResidencyProgram();
  residencyProgramTitle.textContent = result.program.program;
  residencyStatusPill.textContent = result.status;
  residencyStatusPill.dataset.status = result.status.toLowerCase().replace(/\s+/g, "-");
  residencySummary.textContent = result.summary;
  eligibilityScore.textContent = `${Math.round(result.score * 100)}/100`;
  pathwayType.textContent = result.program.pathwayType;
  kycAmlSummary.textContent = result.kycAml;
  privacySummary.textContent = result.privacy;
  incomeValue.textContent = `${currency(state.annualIncome)} household income`;
  assetsValue.textContent = `${currency(state.liquidAssets)} liquid assets`;
  propertyValueLabel.textContent = `${currency(state.propertyValue)} property value`;

  ruleCheckList.innerHTML = result.ruleChecks
    .map((item) => `
      <div class="stack-item">
        <div class="recommendation-topline">
          <strong>${item.name}</strong>
          <span>${item.status}</span>
        </div>
        <p>${item.detail}</p>
      </div>
    `)
    .join("");

  documentCheckList.innerHTML = result.documentChecks
    .map((item) => `
      <div class="stack-item">
        <div class="recommendation-topline">
          <strong>${item.document}</strong>
          <span>${item.status}</span>
        </div>
        <p>${item.detail}</p>
      </div>
    `)
    .join("");

  complianceWorkflowList.innerHTML = result.workflow
    .map((item) => `
      <div class="stack-item">
        <div class="recommendation-topline">
          <strong>${item.step}</strong>
          <span>${item.status}</span>
        </div>
        <p>${item.detail}</p>
        <small>Owner • ${item.owner}</small>
      </div>
    `)
    .join("");
}

function getInsuranceScenario() {
  const profileConfig = insuranceProfiles[state.activeJourney];
  const options = profileConfig.options[state.insurancePropertyType] || profileConfig.options.single_family || profileConfig.options.condo || Object.values(profileConfig.options)[0];
  const optionList = [
    { key: "homeowners", label: state.insurancePropertyType === "multifamily" ? "Property package" : "Homeowners" },
    { key: "titlePolicy", label: "Title" },
    { key: "landlord", label: "Landlord" },
    { key: "life", label: "Life / continuity" }
  ].filter((item) => item.key !== "landlord" || state.insuranceNeedsLandlord)
    .filter((item) => item.key !== "titlePolicy" || state.insuranceNeedsTitle)
    .filter((item) => item.key !== "life" || state.insuranceNeedsLife)
    .map((item) => ({ ...item, ...options[item.key] }));

  const readinessBase = 0.61
    + (state.insuranceNeedsTitle ? 0.06 : 0)
    + (state.insuranceNeedsLife ? 0.05 : 0)
    + (state.insuranceNeedsLandlord ? 0.05 : 0)
    + (state.insuranceOccupancy === "owner_occupied" ? 0.05 : 0)
    + (state.insuranceTransactionContext === "closing" ? 0.04 : state.insuranceTransactionContext === "portfolio" ? -0.02 : 0)
    + (state.risk === "conservative" ? 0.05 : state.risk === "opportunistic" ? -0.02 : 0)
    + (state.insuranceHouseholdRisk === "estate_planning" ? 0.03 : state.insuranceHouseholdRisk === "debt_continuity" ? 0.02 : 0);
  const readiness = Math.max(0.48, Math.min(0.97, readinessBase));
  const status = readiness >= 0.8 ? "Release ready" : readiness >= 0.68 ? "Reviewable" : "Escalate";
  const payload = [
    {
      title: "ACORD intake packet",
      status: profileConfig.secureExchange,
      detail: `Captures applicant, dwelling, occupancy, mortgage, title, and prior-loss fields with the minimum attributes required for ${state.insuranceTransactionContext} workflows.`
    },
    {
      title: "Secure exchange envelope",
      status: "mTLS + field encryption + correlation ID",
      detail: "Outbound servicing traffic uses encrypted transport, message signing, and redaction-aware payload profiles before partner delivery."
    },
    {
      title: "Release governance",
      status: state.explanationDepth === "full" ? "Full evidence packet" : "Scoped decision summary",
      detail: "Quote assumptions, exclusions, carrier appetite, and underwriting blockers are released according to role, consent scope, and privacy tier."
    }
  ];
  const primary = optionList[0];
  return {
    profileConfig,
    options: optionList,
    readiness,
    status,
    summary: `${profileConfig.profileLabel} guidance maps user profile, ${state.insurancePropertyType.replace(/_/g, " ")}, ${state.insuranceTransactionContext} timing, and ${state.insuranceHouseholdRisk.replace(/_/g, " ")} priorities into a policy stack that keeps homeowners, title, landlord, and life-related recommendations visible in one view.`,
    acordMode: profileConfig.secureExchange,
    naicPosture: "Purpose-bound sharing • encrypted exchange • role-based servicing • disposal controls",
    primaryPackage: primary ? primary.title : "Coverage review",
    payload,
    controls: profileConfig.controls
  };
}

function renderInsuranceEngine() {
  const result = getInsuranceScenario();
  insuranceProgramTitle.textContent = result.profileConfig.profileLabel;
  insuranceStatusPill.textContent = result.status;
  insuranceStatusPill.dataset.status = result.status.toLowerCase().replace(/\s+/g, "-");
  insuranceSummary.textContent = result.summary;
  insuranceReadinessScore.textContent = `${Math.round(result.readiness * 100)}/100`;
  insurancePrimaryPackage.textContent = result.primaryPackage;
  insuranceAcordMode.textContent = result.acordMode;
  insuranceNaicPosture.textContent = result.naicPosture;

  insuranceOptionList.innerHTML = result.options
    .map((item) => `
      <div class="stack-item">
        <div class="recommendation-topline">
          <strong>${item.label} • ${item.title}</strong>
          <span>${item.fit} • ${item.premium}</span>
        </div>
        <p>${item.summary}</p>
      </div>
    `)
    .join("");

  insurancePayloadList.innerHTML = result.payload
    .map((item) => `
      <div class="stack-item">
        <div class="recommendation-topline">
          <strong>${item.title}</strong>
          <span>${item.status}</span>
        </div>
        <p>${item.detail}</p>
      </div>
    `)
    .join("");

  insuranceControlList.innerHTML = result.controls
    .map((item, index) => `
      <div class="stack-item">
        <div class="recommendation-topline">
          <strong>Control ${index + 1}</strong>
          <span>NAIC aligned</span>
        </div>
        <p>${item}</p>
      </div>
    `)
    .join("");
}

function getPaymentScenario() {
  const profile = paymentProfiles[state.activeJourney];
  const amountFactor = Math.min(0.24, state.paymentAmount / 500000 * 0.22);
  const crossBorderFactor = state.paymentCrossBorder ? 0.15 : 0.03;
  const methodFactor = state.paymentMethod === "wire" ? 0.14 : state.paymentMethod === "card_token" ? 0.1 : state.paymentMethod === "wallet" ? 0.08 : state.paymentMethod === "escrow_disbursement" ? 0.06 : 0.05;
  const settlementFactor = state.paymentSettlementTiming === "same_day" ? 0.09 : state.paymentSettlementTiming === "manual_hold" ? 0.03 : 0.05;
  const trustAdjustment = state.paymentTrustedDevice ? -0.08 : 0.1;
  const manualAdjustment = state.paymentManualReview ? -0.04 : 0.05;
  const escrowAdjustment = state.paymentEscrowStage === "docs_cleared" || state.paymentEscrowStage === "release_pending" ? -0.03 : state.paymentEscrowStage === "disbursed" ? -0.08 : 0.04;
  const fraudProbability = Math.max(0.04, Math.min(0.94, 0.16 + amountFactor + crossBorderFactor + methodFactor + settlementFactor + trustAdjustment + manualAdjustment + escrowAdjustment));
  const riskLevel = fraudProbability >= 0.72 ? "High review" : fraudProbability >= 0.48 ? "Reviewable" : "Release ready";
  const behavior = fraudProbability >= 0.72 ? "Anomalous velocity" : fraudProbability >= 0.48 ? "Watchlisted behavior" : "Stable payer behavior";
  const escrowStatus = state.paymentEscrowStage === "release_pending" ? "Awaiting dual approval" : state.paymentEscrowStage === "docs_cleared" ? "Ready when funds settle" : state.paymentEscrowStage === "disbursed" ? "Released and logged" : "Funding controls active";
  const frontendSecurity = `PCI DSS hosted fields • ${state.paymentTrustedDevice ? "trusted session binding" : "step-up review needed"}`;
  const signals = [
    {
      title: "Device and session trust",
      status: state.paymentTrustedDevice ? "Pass" : "Review",
      detail: state.paymentTrustedDevice ? "Session is bound to a trusted device, MFA, and a low-friction PSP token exchange." : "Session requires step-up verification because device trust or binding is incomplete."
    },
    {
      title: "Amount and velocity",
      status: state.paymentAmount > 100000 ? "Review" : "Pass",
      detail: `Amount ${currency(state.paymentAmount)} is assessed with payment velocity, beneficiary history, and atypical movement checks.`
    },
    {
      title: "Geography and funding route",
      status: state.paymentCrossBorder ? "Review" : "Pass",
      detail: state.paymentCrossBorder ? "Cross-border movement triggers enhanced sanctions, beneficiary, and settlement-delay analytics." : "Domestic route keeps settlement and sanctions complexity lower."
    },
    {
      title: "Payer behavior model",
      status: state.paymentManualReview ? "Manual review" : fraudProbability >= 0.6 ? "Review" : "Pass",
      detail: `${behavior} is derived from token usage, timing, session posture, and escrow-stage context.`
    }
  ];
  const escrowConditions = [
    {
      title: "Funds availability",
      status: ["funds_received", "docs_cleared", "release_pending", "disbursed"].includes(state.paymentEscrowStage) ? "Ready" : "Pending",
      detail: "Escrow desk confirms cleared funds before release or disbursement instructions can execute."
    },
    {
      title: "Document and milestone clearance",
      status: ["docs_cleared", "release_pending", "disbursed"].includes(state.paymentEscrowStage) ? "Ready" : "Review",
      detail: "Closing documents, identity checks, and approval milestones must all align with the payment action."
    },
    {
      title: "Dual approval and beneficiary match",
      status: state.paymentEscrowStage === "release_pending" || state.paymentEscrowStage === "disbursed" ? "Ready" : "Pending",
      detail: "Release requires beneficiary matching, approver segregation, and immutable escrow event logging."
    }
  ];
  const reconciliation = [
    {
      title: "Authorization to capture match",
      status: state.paymentMethod === "card_token" ? "Tracked" : "Not applicable",
      detail: "Card or wallet paths reconcile PSP authorization and capture references without exposing PAN data."
    },
    {
      title: "Escrow ledger alignment",
      status: state.paymentEscrowStage === "disbursed" ? "Closed" : "Open",
      detail: "Ledger, PSP, bank, and settlement file references are compared to detect mismatches before closeout."
    },
    {
      title: "Settlement exception handling",
      status: state.paymentManualReview ? "Escalated" : "Monitored",
      detail: "Signed webhooks, reconciliation jobs, and operations queues manage exceptions, refunds, and release reversals."
    }
  ];

  return {
    profile,
    fraudProbability,
    status: riskLevel,
    behavior,
    escrowStatus,
    frontendSecurity,
    signals,
    escrowConditions,
    reconciliation,
    summary: `${profile.label} uses ${profile.tokenization} so users complete payment steps inside a PCI-safe frontend shell while backend services score fraud probability, payer behavior, escrow conditions, and reconciliation integrity before release.`,
    controls: profile.controls
  };
}

function renderPaymentEngine() {
  const result = getPaymentScenario();
  paymentProgramTitle.textContent = result.profile.label;
  paymentStatusPill.textContent = result.status;
  paymentStatusPill.dataset.status = result.status.toLowerCase().replace(/\s+/g, "-");
  paymentSummary.textContent = result.summary;
  paymentAmountValue.textContent = `${currency(state.paymentAmount)} payment amount`;
  paymentFraudScore.textContent = `${Math.round(result.fraudProbability * 100)}% probability`;
  paymentBehaviorSummary.textContent = result.behavior;
  paymentEscrowSummary.textContent = result.escrowStatus;
  paymentFrontendPosture.textContent = result.frontendSecurity;

  paymentSignalList.innerHTML = result.signals
    .map((item) => `
      <div class="stack-item">
        <div class="recommendation-topline">
          <strong>${item.title}</strong>
          <span>${item.status}</span>
        </div>
        <p>${item.detail}</p>
      </div>
    `)
    .join("");

  paymentEscrowList.innerHTML = result.escrowConditions
    .map((item) => `
      <div class="stack-item">
        <div class="recommendation-topline">
          <strong>${item.title}</strong>
          <span>${item.status}</span>
        </div>
        <p>${item.detail}</p>
      </div>
    `)
    .join("");

  paymentReconciliationList.innerHTML = [...result.reconciliation, ...result.controls.map((item, index) => ({ title: `PCI / ops control ${index + 1}`, status: "Active", detail: item }))]
    .map((item) => `
      <div class="stack-item">
        <div class="recommendation-topline">
          <strong>${item.title}</strong>
          <span>${item.status}</span>
        </div>
        <p>${item.detail}</p>
      </div>
    `)
    .join("");
}

function getIntegrationScenario() {
  const profile = integrationProfiles[state.integrationPartner];
  const releaseStatus = state.explanationDepth === "full" || state.activeJourney === "advisor" ? "Evidence ready" : state.integrationPartner === "government_registry" ? "Jurisdiction review" : "Release ready";
  return {
    ...profile,
    releaseStatus
  };
}

function renderIntegrationHub() {
  const result = getIntegrationScenario();
  integrationProgramTitle.textContent = result.label;
  integrationStatusPill.textContent = result.releaseStatus;
  integrationStatusPill.dataset.status = result.releaseStatus.toLowerCase().replace(/\s+/g, "-");
  integrationSummary.textContent = result.summary;
  integrationCanonicalModel.textContent = result.canonicalModel;
  integrationExpertChain.textContent = result.expertChain.join(" → ");
  integrationSecurityPosture.textContent = result.security;
  integrationRouteTarget.textContent = result.routeTarget;

  integrationControlList.innerHTML = result.controls
    .map((item) => `
      <div class="stack-item">
        <div class="recommendation-topline">
          <strong>${item.title}</strong>
          <span>${item.status}</span>
        </div>
        <p>${item.detail}</p>
      </div>
    `)
    .join("");

  integrationRouteList.innerHTML = result.routes
    .map((item) => `
      <div class="stack-item">
        <div class="recommendation-topline">
          <strong>${item.title}</strong>
          <span>${item.status}</span>
        </div>
        <p>${item.detail}</p>
      </div>
    `)
    .join("");

  integrationEvidenceList.innerHTML = result.evidence
    .map((item) => `
      <div class="stack-item">
        <div class="recommendation-topline">
          <strong>${item.title}</strong>
          <span>${item.status}</span>
        </div>
        <p>${item.detail}</p>
      </div>
    `)
    .join("");
}

function renderNextActions(journey, topCandidate) {
  const dynamicActions = [
    ...journey.nextActions,
    ...journey.deal.experts.slice(0, 2).map((item) => item.summary),
    `Review why ${topCandidate.title} outranked alternatives before sharing externally.`
  ];

  nextActionsList.innerHTML = dynamicActions
    .map(
      (item) => `
        <div class="stack-item action-item">
          <strong>Next action</strong>
          <p>${item}</p>
        </div>
      `
    )
    .join("");
}

function renderJourney() {
  const journey = journeys[state.activeJourney];
  const rankedCandidates = rankCandidates();
  const topCandidate = rankedCandidates[0];

  title.textContent = journey.title;
  summary.textContent = journey.summary;
  confidence.textContent = topCandidate.aggregateScore.toFixed(2);
  releaseStatus.textContent = getReleaseTone();
  headline.textContent = journey.headline;
  subtitle.textContent = journey.subtitle;
  investorType.textContent = journey.profile.investorType;
  locationValue.textContent = journey.profile.location;
  financialIntent.textContent = journey.profile.financialIntent;
  residencyGoal.textContent = state.residency ? journey.profile.residencyGoal : "Not currently prioritized";
  accessState.textContent = journey.profile.access;

  action.textContent = buildActionText(topCandidate);
  risk.textContent = buildRiskText(topCandidate);
  why.textContent = buildWhyText(topCandidate);

  steps.innerHTML = journey.steps.map((item) => `<li>${item}</li>`).join("");

  const weights = buildWeights();
  expertStrip.innerHTML = Object.entries(weights)
    .sort((a, b) => b[1] - a[1])
    .map(([key, value]) => `<span class="expert-pill">${expertMeta[key].icon} ${Math.round(value * 100)}%</span>`)
    .join("");

  renderPropertyList(rankedCandidates);
  renderInsights(rankedCandidates);
  renderValuation(rankedCandidates);
  renderGovernance();
  renderContributions(topCandidate);
  renderDealBoard();
  renderResidencyEngine();
  renderInsuranceEngine();
  renderPaymentEngine();
  renderIntegrationHub();
  renderNextActions(journey, topCandidate);

  budgetValue.textContent = `${currency(state.budget)} budget cap`;

  journeyButtons.forEach((card) => {
    const isActive = card.dataset.journey === state.activeJourney;
    card.classList.toggle("active", isActive);
    card.setAttribute("aria-selected", String(isActive));
  });
}

journeyButtons.forEach((card) => {
  card.addEventListener("click", () => {
    applyJourneyDefaults(card.dataset.journey);
    renderJourney();
  });
});

personaSelect.addEventListener("change", (event) => {
  applyJourneyDefaults(event.target.value);
  renderJourney();
});

objectiveSelect.addEventListener("change", (event) => {
  state.objective = event.target.value;
  renderJourney();
});

riskSelect.addEventListener("change", (event) => {
  state.risk = event.target.value;
  renderJourney();
});

explanationSelect.addEventListener("change", (event) => {
  state.explanationDepth = event.target.value;
  renderJourney();
});

budgetRange.addEventListener("input", (event) => {
  state.budget = Number(event.target.value);
  renderJourney();
});

residencyToggle.addEventListener("change", (event) => {
  state.residency = event.target.checked;
  renderJourney();
});

financingToggle.addEventListener("change", (event) => {
  state.financing = event.target.checked;
  renderJourney();
});

jurisdictionSelect.addEventListener("change", (event) => {
  state.jurisdiction = event.target.value;
  renderJourney();
});

incomeRange.addEventListener("input", (event) => {
  state.annualIncome = Number(event.target.value);
  renderJourney();
});

assetsRange.addEventListener("input", (event) => {
  state.liquidAssets = Number(event.target.value);
  renderJourney();
});

propertyValueRange.addEventListener("input", (event) => {
  state.propertyValue = Number(event.target.value);
  renderJourney();
});

sourceOfFundsToggle.addEventListener("change", (event) => {
  state.sourceOfFundsVerified = event.target.checked;
  renderJourney();
});

criminalRecordToggle.addEventListener("change", (event) => {
  state.criminalRecordClear = event.target.checked;
  renderJourney();
});

healthInsuranceToggle.addEventListener("change", (event) => {
  state.healthInsuranceReady = event.target.checked;
  renderJourney();
});

insurancePropertyType.addEventListener("change", (event) => {
  state.insurancePropertyType = event.target.value;
  renderJourney();
});

insuranceTransactionContext.addEventListener("change", (event) => {
  state.insuranceTransactionContext = event.target.value;
  renderJourney();
});

insuranceOccupancy.addEventListener("change", (event) => {
  state.insuranceOccupancy = event.target.value;
  renderJourney();
});

insuranceHouseholdRisk.addEventListener("change", (event) => {
  state.insuranceHouseholdRisk = event.target.value;
  renderJourney();
});

insuranceTitleToggle.addEventListener("change", (event) => {
  state.insuranceNeedsTitle = event.target.checked;
  renderJourney();
});

insuranceLandlordToggle.addEventListener("change", (event) => {
  state.insuranceNeedsLandlord = event.target.checked;
  renderJourney();
});

insuranceLifeToggle.addEventListener("change", (event) => {
  state.insuranceNeedsLife = event.target.checked;
  renderJourney();
});

paymentMethodSelect.addEventListener("change", (event) => {
  state.paymentMethod = event.target.value;
  renderJourney();
});

paymentEscrowStage.addEventListener("change", (event) => {
  state.paymentEscrowStage = event.target.value;
  renderJourney();
});

paymentAmountRange.addEventListener("input", (event) => {
  state.paymentAmount = Number(event.target.value);
  renderJourney();
});

paymentSettlementSelect.addEventListener("change", (event) => {
  state.paymentSettlementTiming = event.target.value;
  renderJourney();
});

paymentDeviceTrusted.addEventListener("change", (event) => {
  state.paymentTrustedDevice = event.target.checked;
  renderJourney();
});

paymentCrossBorder.addEventListener("change", (event) => {
  state.paymentCrossBorder = event.target.checked;
  renderJourney();
});

paymentManualReview.addEventListener("change", (event) => {
  state.paymentManualReview = event.target.checked;
  renderJourney();
});

integrationPartnerSelect.addEventListener("change", (event) => {
  state.integrationPartner = event.target.value;
  renderJourney();
});

populateStaticControls();
applyJourneyDefaults("buyer");
renderJourney();
