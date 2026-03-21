const journeys = {
  buyer: {
    title: "Buyer journey",
    summary: "Balanced recommendations for livability, affordability, relocation readiness, and transaction certainty.",
    confidence: 0.94,
    releaseStatus: "Ready with transaction review",
    headline: "Personalized shortlist shaped by property, finance, visa, insurance, pricing, and transaction experts",
    subtitle: "The workspace reflects the target Next.js product surface while keeping property guidance, expert routing, and deal execution in the same flow.",
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
    subtitle: "Investors get richer downside framing, explainability, and stage-aware controls before capital is committed.",
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

const copilotRoleLibrary = {
  buyer_advisor: {
    title: "Buyer advisor",
    focus: "Affordability, relocation readiness, and guided next steps."
  },
  investor_strategist: {
    title: "Investor strategist",
    focus: "Return resilience, downside framing, and market timing."
  },
  insurance_guide: {
    title: "Insurance guide",
    focus: "Coverage structure, underwriting readiness, and quote controls."
  },
  visa_assistant: {
    title: "Visa assistant",
    focus: "Eligibility, document gaps, and filing readiness."
  },
  compliance_explainer: {
    title: "Compliance explainer",
    focus: "Release gates, audit evidence, privacy, and explainability."
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

const marketIntelligenceProfiles = {
  buyer: {
    scope: "Portugal relocation corridor",
    horizon: "18 months",
    strategyBias: "Capital preservation with relocation optionality",
    signalSummary: "Migration-led family demand and constrained Lisbon supply keep pricing resilient while a flatter rate path improves financing clarity.",
    streams: [
      "Daily macro rate and mortgage spread feed for affordability and refinancing signals.",
      "Weekly relocation and migration ledger tracking family inflows, visa demand, and school-led moves.",
      "Daily Lisbon inventory and absorption monitor for supply-demand imbalance detection."
    ],
    forecasts: [
      "6-month view: pricing remains resilient and rent growth stays positive as inventory stays tight.",
      "12-month view: easing affordability pressure supports owner-occupier demand in relocation-friendly districts.",
      "Alert: neighborhoods with strong transit and school access should be prioritized when new supply stays constrained."
    ],
    pipeline: [
      "Streaming ingest normalizes macro, local listing, migration, and affordability feeds.",
      "Forecasting models retrain weekly with drift checks before publishing frontend alerts.",
      "Investor, broker, and analyst surfaces receive explainable signals instead of raw black-box scores."
    ]
  },
  investor: {
    scope: "Mediterranean income markets",
    horizon: "24 months",
    strategyBias: "Income resilience and optional residency",
    signalSummary: "Athens and Lisbon remain supported by migration and rental absorption, while rate easing improves cash-flow resilience for leveraged buyers.",
    streams: [
      "Daily global rates, FX, and inflation feeds for cap-rate and financing pressure modeling.",
      "Weekly migration and investor mobility ledger across Greece, Portugal, and UAE corridors.",
      "Daily supply-demand monitor covering inventory, absorption, concessions, and rent velocity."
    ],
    forecasts: [
      "6-month view: yield strategies remain favored where supply tightness outpaces new completions.",
      "12-month view: rents should stay constructive in gateway districts supported by cross-border inflows.",
      "Alert: spread compression improves acquisition timing, but only for assets with resilient downside underwriting."
    ],
    pipeline: [
      "Cross-market feature engineering combines rates, migration, supply, and liquidity signals.",
      "Champion-challenger forecasting models retrain weekly and publish horizon-specific confidence scores.",
      "Signals are shipped into investor watchlists and opportunity alerts for brokers and analysts."
    ]
  },
  advisor: {
    scope: "Advisor watchlist: Greece, Spain, UAE",
    horizon: "12 months",
    strategyBias: "Risk-gated allocation and client memoing",
    signalSummary: "Macro conditions are improving, but advisors should focus on markets where migration demand remains durable and supply imbalances are still explainable to clients.",
    streams: [
      "Daily macro and credit feeds for rate-path, liquidity, and affordability scenario updates.",
      "Weekly mobility and residency-intent signals for client demand clustering and jurisdiction watchlists.",
      "Daily local supply, permit, and concession data for memo-ready downside framing."
    ],
    forecasts: [
      "6-month view: advisory memos can lean cautiously constructive in gateway submarkets with disciplined supply.",
      "12-month view: select income assets should benefit from better financing and persistent renter demand.",
      "Alert: policy or rate volatility should trigger memo refreshes before client recommendations are exported."
    ],
    pipeline: [
      "Analyst-facing ingestion continuously refreshes macro, migration, and local inventory signals.",
      "Forecast validation compares active scenarios against prior memo assumptions and drift thresholds.",
      "Published alerts are routed to broker and analyst consoles with clear rationale and severity labels."
    ]
  }
};

const documentIntelligenceProfiles = {
  buyer: {
    portfolioName: "Buyer-side legal packet",
    documents: 4,
    status: "Guided review",
    summary: "Contracts, title, insurance, and residency packets are simplified into buyer-friendly explanations while backend validation keeps release gating, anomaly checks, and legal review evidence intact.",
    insights: [
      "The contract is mostly complete, but one attachment still blocks a clean release.",
      "Title evidence is clean and remains the strongest document signal in the packet.",
      "Insurance and residency evidence are understandable in the UI without exposing the raw records."
    ],
    validation: [
      "Extraction confidence stays high because price, title status, coverage amount, and pathway type are normalized across the packet.",
      "Document completeness and date consistency checks run before any buyer-facing release or partner submission."
    ],
    governance: [
      "Medium anomaly posture because binder release should remain coupled to contract completeness.",
      "Immutable audit records preserve ingestion, extraction, compliance linkage, and frontend publication events."
    ]
  },
  investor: {
    portfolioName: "Investor diligence packet",
    documents: 4,
    status: "Analyst review",
    summary: "The frontend gets simplified diligence notes, but the backend still performs cross-document extraction, anomaly detection, and compliance-linked legal reasoning across contracts, title, coverage, and immigration evidence.",
    insights: [
      "Title and core economic terms are easy to inspect in plain language.",
      "Insurance and residency dependencies remain visible as structured blockers rather than buried PDF details.",
      "Anomaly scoring helps investors understand what still requires counsel or advisor review."
    ],
    validation: [
      "Field normalization compares values across legal, insurance, and immigration artifacts before they are surfaced.",
      "Backend checks preserve severity labels so review queues can prioritize material issues first."
    ],
    governance: [
      "Medium anomaly posture due to unresolved evidence dependencies and release sequencing.",
      "Audit and compliance trails stay aligned to cross-border KYC, AML, privacy, and explainability controls."
    ]
  },
  advisor: {
    portfolioName: "Advisor exception packet",
    documents: 4,
    status: "Exception-led review",
    summary: "Advisors see a concise issue list, confidence-backed field extraction, and compliance-linked anomaly reasoning instead of manually reconciling every raw document artifact.",
    insights: [
      "The AI layer explains what changed across the packet and why an exception matters.",
      "Compliance, insurance, and residency evidence stay tied to the transaction audit chain.",
      "Advisors can challenge extraction results using the attached rationale and confidence metadata."
    ],
    validation: [
      "Cross-document comparisons focus on dates, values, signatures, obligations, and evidence dependencies.",
      "Severity labels help route contract, title, insurance, and immigration exceptions to the right operators."
    ],
    governance: [
      "Anomaly posture stays review-focused until all release dependencies are closed.",
      "Full audit chains support legal sign-off, compliance escalation, and downstream regulator readiness."
    ]
  }
};

const state = {
  activeJourney: "buyer",
  activeCopilotRole: "buyer_advisor",
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
  integrationPartner: "banking_core",
  twinOccupancy: 0.94,
  twinMonthlyRent: 3200,
  twinRenovationBudget: 38000,
  twinInsurancePremium: 2256,
  twinHoldYears: 7,
  twinAppreciationRate: 0.031,
  twinOperatingExpenseRatio: 0.28,
  twinFinancingRatio: 0.68,
  twinInterestRate: 0.047
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
const copilotTitle = document.getElementById("copilot-title");
const copilotStatusPill = document.getElementById("copilot-status-pill");
const copilotSummary = document.getElementById("copilot-summary");
const copilotRoleStrip = document.getElementById("copilot-role-strip");
const copilotConversation = document.getElementById("copilot-conversation");
const copilotMemoryList = document.getElementById("copilot-memory-list");
const copilotReasoningList = document.getElementById("copilot-reasoning-list");
const copilotGuardrailList = document.getElementById("copilot-guardrail-list");
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
const complianceGraphTitle = document.getElementById("compliance-graph-title");
const complianceGraphStatus = document.getElementById("compliance-graph-status");
const complianceGraphSummary = document.getElementById("compliance-graph-summary");
const complianceGraphVersion = document.getElementById("compliance-graph-version");
const complianceGraphJurisdictions = document.getElementById("compliance-graph-jurisdictions");
const complianceDomainList = document.getElementById("compliance-domain-list");
const complianceAdaptationList = document.getElementById("compliance-adaptation-list");
const complianceChangeList = document.getElementById("compliance-change-list");
const complianceTransparencyList = document.getElementById("compliance-transparency-list");
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
const twinTitle = document.getElementById("twin-title");
const twinStatusPill = document.getElementById("twin-status-pill");
const twinSummary = document.getElementById("twin-summary");
const twinOccupancyRange = document.getElementById("twin-occupancy-range");
const twinOccupancyValue = document.getElementById("twin-occupancy-value");
const twinRentRange = document.getElementById("twin-rent-range");
const twinRentValue = document.getElementById("twin-rent-value");
const twinRenovationRange = document.getElementById("twin-renovation-range");
const twinRenovationValue = document.getElementById("twin-renovation-value");
const twinInsuranceRange = document.getElementById("twin-insurance-range");
const twinInsuranceValue = document.getElementById("twin-insurance-value");
const twinHoldRange = document.getElementById("twin-hold-range");
const twinHoldValue = document.getElementById("twin-hold-value");
const twinNoi = document.getElementById("twin-noi");
const twinCashflow = document.getElementById("twin-cashflow");
const twinExitValue = document.getElementById("twin-exit-value");
const twinReliability = document.getElementById("twin-reliability");
const twinScenarioList = document.getElementById("twin-scenario-list");
const twinOutlookList = document.getElementById("twin-outlook-list");
const twinGovernanceList = document.getElementById("twin-governance-list");
const marketProgramTitle = document.getElementById("market-program-title");
const marketStatusPill = document.getElementById("market-status-pill");
const marketSummary = document.getElementById("market-summary");
const marketScope = document.getElementById("market-scope");
const marketHorizon = document.getElementById("market-horizon");
const marketStrategyBias = document.getElementById("market-strategy-bias");
const marketSignalSummary = document.getElementById("market-signal-summary");
const marketStreamList = document.getElementById("market-stream-list");
const marketForecastList = document.getElementById("market-forecast-list");
const marketPipelineList = document.getElementById("market-pipeline-list");
const documentProgramTitle = document.getElementById("document-program-title");
const documentStatusPill = document.getElementById("document-status-pill");
const documentSummary = document.getElementById("document-summary");
const documentPortfolioName = document.getElementById("document-portfolio-name");
const documentCount = document.getElementById("document-count");
const documentAnomalySummary = document.getElementById("document-anomaly-summary");
const documentAuditSummary = document.getElementById("document-audit-summary");
const documentInsightList = document.getElementById("document-insight-list");
const documentValidationList = document.getElementById("document-validation-list");
const documentGovernanceList = document.getElementById("document-governance-list");
const wiringTitle = document.getElementById("wiring-title");
const wiringStatusPill = document.getElementById("wiring-status-pill");
const wiringSummary = document.getElementById("wiring-summary");
const wiringCardGrid = document.getElementById("wiring-card-grid");

const backendSnapshot = {
  status: "loading",
  data: null,
  error: null
};

function getBackendPackets() {
  if (backendSnapshot.status !== "ready") return null;

  const journeyPackets = backendSnapshot.data?.journeys?.[state.activeJourney]?.packets;
  return journeyPackets || backendSnapshot.data?.packets || null;
}

function getBackendSync() {
  const packets = getBackendPackets();
  if (!packets) return null;

  return {
    journeyKey: packets.journey_key || state.activeJourney,
    property: packets.property_decision,
    transaction: packets.transaction_decision,
    payment: packets.payment_decision,
    insurance: packets.insurance_decision,
    integration: packets.integration_decision,
    residency: packets.residency_decision,
    complianceGraph: packets.compliance_graph_decision,
    digitalTwin: packets.digital_twin_decision,
    marketIntelligence: packets.market_intelligence_decision,
    documentIntelligence: packets.document_intelligence_decision,
    copilot: packets.copilot_decision
  };
}

function currency(value) {
  return new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    maximumFractionDigits: 0
  }).format(value);
}

function createWiringMetricCard(titleText, statusText, detailText) {
  return `
    <article class="decision-card wiring-card">
      <div class="wiring-metric">
        <span>${titleText}</span>
        <strong>${statusText}</strong>
        <p>${detailText}</p>
      </div>
    </article>
  `;
}

function renderWiringStatus() {
  if (backendSnapshot.status === "ready" && backendSnapshot.data?.packets) {
    const packets = getBackendPackets();
    const propertyPacket = packets.property_decision;
    const transactionPacket = packets.transaction_decision;
    const paymentPacket = packets.payment_decision;
    const insurancePacket = packets.insurance_decision;
    const integrationPacket = packets.integration_decision;
    const residencyPacket = packets.residency_decision;
    const complianceGraphPacket = packets.compliance_graph_decision;
    const digitalTwinPacket = packets.digital_twin_decision;
    const marketPacket = packets.market_intelligence_decision;
    const documentPacket = packets.document_intelligence_decision;
    const copilotPacket = packets.copilot_decision;

    wiringTitle.textContent = "Backend snapshot connected";
    wiringStatusPill.textContent = `${state.activeJourney} packets loaded`;
    wiringStatusPill.dataset.status = "loaded";
    wiringSummary.textContent = `Loaded ${backendSnapshot.data.meta.generated_from} and hydrated the ${state.activeJourney} UI with release, risk, and routing signals from the Python orchestration reference. Generated ${backendSnapshot.data.meta.generated_at_utc}.`;
    wiringCardGrid.innerHTML = [
      createWiringMetricCard(
        "Property decision",
        propertyPacket.release_status,
        `${propertyPacket.selected_experts.length} experts selected • ${propertyPacket.ranked_recommendations.length} ranked recommendations.`
      ),
      createWiringMetricCard(
        "Transaction decision",
        `${transactionPacket.risk_rating} risk`,
        `Release ${transactionPacket.release_status} • ${transactionPacket.compliance_controls.length} controls tracked.`
      ),
      createWiringMetricCard(
        "Payment decision",
        paymentPacket.risk_level,
        `${Math.round(paymentPacket.fraud_probability * 100)}% fraud probability • ${paymentPacket.escrow_status}.`
      ),
      createWiringMetricCard(
        "Insurance decision",
        insurancePacket.release_status,
        `${insurancePacket.recommendations.length} recommendations • ${insurancePacket.secure_exchange_controls.length} exchange controls.`
      ),
      createWiringMetricCard(
        "Residency decision",
        residencyPacket.eligibility_status,
        `${Math.round(residencyPacket.eligibility_score * 100)}/100 eligibility • ${residencyPacket.jurisdiction}.`
      ),
      createWiringMetricCard(
        "Compliance graph",
        complianceGraphPacket.overall_status,
        `${complianceGraphPacket.domains.length} domains • ${complianceGraphPacket.operating_jurisdictions.join(" → ")}.`
      ),
      createWiringMetricCard(
        "Integration routing",
        integrationPacket.release_status,
        `${integrationPacket.partner_system} → ${integrationPacket.routing_decisions[0].target}.`
      ),
      createWiringMetricCard(
        "Digital twin",
        `${digitalTwinPacket.scenarios.length} scenarios`,
        `${digitalTwinPacket.twin.property_name} • ${digitalTwinPacket.standards_alignment.slice(0, 2).join(" + ")}.`
      ),
      createWiringMetricCard(
        "Market intelligence",
        `${marketPacket.forecasts.length} forecasts`,
        `${marketPacket.market_scope} • ${marketPacket.alerts.length} alerts live.`
      ),
      createWiringMetricCard(
        "Document intelligence",
        documentPacket.release_status,
        `${documentPacket.governed_documents.length} documents • ${documentPacket.anomaly_signals.length} anomaly signals traced.`
      ),
      createWiringMetricCard(
        "Conversational copilot",
        `${copilotPacket.roles.length} roles`,
        `${copilotPacket.active_role.replace(/_/g, " ")} active • ${copilotPacket.guardrails.length} guardrails traced.`
      )
    ].join("");
    return;
  }

  wiringTitle.textContent = backendSnapshot.status === "error" ? "Backend snapshot unavailable" : "Frontend fallback mode";
  wiringStatusPill.textContent = backendSnapshot.status === "error" ? "Using local fallback data" : "Waiting for backend snapshot";
  wiringStatusPill.dataset.status = backendSnapshot.status;
  wiringSummary.textContent =
    backendSnapshot.status === "error"
      ? `Could not load frontend/demo-packets.json, so the UI is using in-browser reference data only. ${backendSnapshot.error || ""}`.trim()
      : "The frontend is ready to hydrate against backend orchestration packets once a generated demo snapshot is available.";
  wiringCardGrid.innerHTML = [
    createWiringMetricCard("Property decision", "Local prototype", "Frontend ranking and explainability remain interactive while the backend snapshot is unavailable."),
    createWiringMetricCard("Transaction decision", "Local prototype", "Deal controls, stage tracking, and workflow evidence are still rendered from browser-side defaults."),
    createWiringMetricCard("Specialized engines", "Awaiting sync", "Residency, insurance, payments, integration routing, digital twin simulation, predictive market signals, document intelligence, and conversational copilot roles will promote backend statuses when the snapshot loads.")
  ].join("");
}

async function loadBackendSnapshot() {
  try {
    const response = await fetch("./demo-packets.json", { cache: "no-store" });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    backendSnapshot.data = await response.json();
    backendSnapshot.status = "ready";
  } catch (error) {
    backendSnapshot.status = "error";
    backendSnapshot.error = error.message;
  }
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
  state.activeCopilotRole = journeyKey === "investor" ? "investor_strategist" : journeyKey === "advisor" ? "compliance_explainer" : "buyer_advisor";
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
  state.twinOccupancy = journeyKey === "investor" ? 0.91 : journeyKey === "advisor" ? 0.93 : 0.94;
  state.twinMonthlyRent = journeyKey === "investor" ? 6150 : journeyKey === "advisor" ? 6400 : 3200;
  state.twinRenovationBudget = journeyKey === "investor" ? 95000 : journeyKey === "advisor" ? 76000 : 38000;
  state.twinInsurancePremium = journeyKey === "investor" ? 3864 : journeyKey === "advisor" ? 4020 : 2256;
  state.twinHoldYears = journeyKey === "investor" ? 8 : journeyKey === "advisor" ? 6 : 7;
  state.twinAppreciationRate = journeyKey === "investor" ? 0.036 : journeyKey === "advisor" ? 0.034 : 0.031;
  state.twinOperatingExpenseRatio = journeyKey === "investor" ? 0.32 : journeyKey === "advisor" ? 0.3 : 0.28;
  state.twinFinancingRatio = journeyKey === "investor" ? 0.48 : journeyKey === "advisor" ? 0.42 : 0.68;
  state.twinInterestRate = journeyKey === "investor" ? 0.052 : journeyKey === "advisor" ? 0.049 : 0.047;
  paymentMethodSelect.value = state.paymentMethod;
  paymentEscrowStage.value = state.paymentEscrowStage;
  paymentAmountRange.value = state.paymentAmount;
  paymentSettlementSelect.value = state.paymentSettlementTiming;
  paymentDeviceTrusted.checked = state.paymentTrustedDevice;
  paymentCrossBorder.checked = state.paymentCrossBorder;
  paymentManualReview.checked = state.paymentManualReview;
  integrationPartnerSelect.value = state.integrationPartner;
  twinOccupancyRange.value = state.twinOccupancy;
  twinRentRange.value = state.twinMonthlyRent;
  twinRenovationRange.value = state.twinRenovationBudget;
  twinInsuranceRange.value = state.twinInsurancePremium;
  twinHoldRange.value = state.twinHoldYears;
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
  const backend = getBackendSync();
  if (backend?.property?.ranked_recommendations?.length) {
    propertyList.innerHTML = backend.property.ranked_recommendations
      .map((candidate, index) => {
        const delta = Math.round(candidate.composite_score * 100);
        return `
          <article class="recommendation-item ${index === 0 ? "recommendation-item--featured" : ""}">
            <div class="recommendation-topline">
              <strong>#${index + 1} ${candidate.title}</strong>
              <span>${candidate.geography}</span>
            </div>
            <p>${candidate.summary}</p>
            <div class="meta-row">
              <span>Confidence ${Math.round(candidate.confidence * 100)}/100</span>
              <span>Score ${delta}/100</span>
              <span>Value band ${candidate.valuation_band}</span>
            </div>
            <div class="tag-row">
              ${Object.entries(candidate.expert_contributions)
                .slice(0, 4)
                .map(([key, value]) => `<span>${key.replace(/_/g, " ")} ${Math.round(value * 100)}/100</span>`)
                .join("")}
            </div>
            <p class="helper-copy">${candidate.why}</p>
          </article>
        `;
      })
      .join("");
    propertyFitPill.textContent = `Top match: ${backend.property.ranked_recommendations[0].geography}`;
    return;
  }

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
  const backend = getBackendSync();
  if (backend?.property?.ranked_recommendations?.length) {
    const recommendations = backend.property.ranked_recommendations.slice(0, 2);
    insightList.innerHTML = recommendations
      .map(
        (candidate) => `
          <div class="stack-item">
            <strong>${candidate.title}</strong>
            <p>${candidate.investment_insight}</p>
          </div>
        `
      )
      .join("");

    visaList.innerHTML = recommendations
      .map(
        (candidate) => `
          <div class="stack-item">
            <strong>${candidate.title} • Residency path</strong>
            <span>Backend packet</span>
            <p>${candidate.visa_pathway}</p>
          </div>
        `
      )
      .join("");

    insuranceList.innerHTML = recommendations
      .map(
        (candidate) => `
          <div class="stack-item">
            <strong>${candidate.title} • Insurance signal</strong>
            <span>Backend packet</span>
            <p>${candidate.insurance_option}</p>
          </div>
        `
      )
      .join("");
    return;
  }

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
  const backend = getBackendSync();
  if (backend?.property?.ranked_recommendations?.length) {
    valuationList.innerHTML = backend.property.ranked_recommendations
      .slice(0, 2)
      .map((candidate) => {
        return `
          <div class="stack-item">
            <strong>${candidate.title} • ${candidate.valuation_band}</strong>
            <span>${candidate.comparable_summary}</span>
            <p>${candidate.trend_signal} ${candidate.location_intelligence}</p>
          </div>
        `;
      })
      .join("");
    return;
  }

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
  const backend = getBackendSync();
  if (backend?.property?.governance_status?.length) {
    governanceList.innerHTML = backend.property.governance_status
      .map(
        (profile) => `
        <div class="stack-item">
          <strong>${profile.framework} • ${profile.status}</strong>
          <span>${profile.controls.join(" • ")}</span>
          <p>${profile.explanation}</p>
        </div>
      `
      )
      .join("");
    return;
  }

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
  const backend = getBackendSync();
  const backendTopCandidate = backend?.property?.ranked_recommendations?.[0];
  if (backendTopCandidate) {
    contributionList.innerHTML = Object.entries(backendTopCandidate.expert_contributions)
      .sort((a, b) => b[1] - a[1])
      .map(([key, value]) => {
        const percent = Math.round(value * 100);
        const label = key.replace(/_/g, " ");
        return `
          <div class="stack-item contribution-item">
            <div class="contribution-header">
              <strong>${label}</strong>
              <span>${percent}/100</span>
            </div>
            <div class="progress-track"><span style="width:${Math.max(percent, 8)}%"></span></div>
            <p>Backend orchestration contribution from ${label} for ${backendTopCandidate.title}.</p>
          </div>
        `;
      })
      .join("");
    return;
  }

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

function buildLocalCopilotData(journey, topCandidate) {
  const activeRole = state.activeCopilotRole;
  const roleEntries = Object.entries(copilotRoleLibrary).map(([roleKey, meta]) => ({
    role_key: roleKey,
    title: meta.title,
    focus: meta.focus,
    confidence: roleKey === activeRole ? Number((topCandidate.aggregateScore || 0.9).toFixed(2)) : Number((Math.max((topCandidate.aggregateScore || 0.9) - 0.05, 0.72)).toFixed(2)),
    summary:
      roleKey === "buyer_advisor"
        ? `${topCandidate.title} is framed around household fit, financing comfort, and relocation readiness.`
        : roleKey === "investor_strategist"
          ? `${topCandidate.title} is translated into resilient yield, macro timing, and downside language.`
          : roleKey === "insurance_guide"
            ? `Coverage advice focuses on ${topCandidate.insurance.title.toLowerCase()} and the documentation needed to place it safely.`
            : roleKey === "visa_assistant"
              ? `Residency guidance keeps ${topCandidate.visaPathway.title.toLowerCase()} and document readiness in focus.`
              : `Control notes explain why ${topCandidate.title} remains releaseable under the current risk and privacy posture.`
  }));

  return {
    active_role: activeRole,
    roles: roleEntries,
    conversation: [
      {
        speaker: "user",
        role: copilotRoleLibrary[activeRole].title,
        text: `Help me understand why ${topCandidate.title} is the right next step for my ${journey.title.toLowerCase()}.`,
        sources: ["Adaptive intake", "Journey defaults"]
      },
      {
        speaker: "assistant",
        role: copilotRoleLibrary[activeRole].title,
        text: `${topCandidate.why} I am using the ${copilotRoleLibrary[activeRole].title.toLowerCase()} lens so the answer matches your current objective and explanation depth.`,
        sources: ["Ranked shortlist", "Role-specific framing"]
      },
      {
        speaker: "assistant",
        role: "Compliance explainer",
        text: `Release confidence remains ${getReleaseTone().toLowerCase()}, and the explanation stays privacy-aware by surfacing only role-appropriate reasoning, memory, and next actions.`,
        sources: ["Release posture", "Privacy controls"]
      }
    ],
    memory: [
      { label: "Persona", value: journey.title, source: "Journey state", retention: "Session" },
      { label: "Objective", value: state.objective, source: "Adaptive controls", retention: "Session" },
      { label: "Budget", value: currency(state.budget), source: "Adaptive controls", retention: "Session" },
      { label: "Top listing", value: topCandidate.title, source: "Ranked shortlist", retention: "Decision record" },
      { label: "Residency preference", value: state.residency ? "Enabled" : "Not prioritized", source: "Adaptive controls", retention: "Session" }
    ],
    reasoning_trace: [
      {
        step: "Role selection",
        experts: ["UX personalization", "Conversational copilot"],
        detail: `The copilot activates the ${copilotRoleLibrary[activeRole].title.toLowerCase()} voice to match the current journey and explanation depth.`
      },
      {
        step: "Evidence synthesis",
        experts: ["Property expert", "Finance expert", "Compliance expert"],
        detail: `Property fit, financing posture, and compliance confidence are combined before any natural-language answer is drafted.`
      },
      {
        step: "Guarded response",
        experts: ["Compliance expert", "Recommendation expert"],
        detail: `Only explainable, policy-safe details are released so the chat stays useful without bypassing privacy or control gates.`
      }
    ],
    guardrails: [
      {
        control: "Short-term memory minimization",
        status: "Active",
        detail: "The prototype stores only intent, budget, and released recommendation context inside the conversational surface."
      },
      {
        control: "Role-specific reasoning",
        status: "Active",
        detail: "Buyer, investor, insurance, visa, and compliance modes share the same facts but change the framing and next-best actions."
      },
      {
        control: "Explainable release",
        status: "Active",
        detail: "Every answer ties back to recommendation rationale, risk posture, or governed workflow evidence."
      }
    ],
    recommended_actions: journey.nextActions
  };
}

function renderCopilot(journey, topCandidate) {
  const backend = getBackendSync();
  const packet = backend?.copilot || buildLocalCopilotData(journey, topCandidate);
  const activeRole = packet.roles.some((role) => role.role_key === state.activeCopilotRole)
    ? state.activeCopilotRole
    : packet.active_role || state.activeCopilotRole;
  const activeSummary = packet.roles.find((role) => role.role_key === activeRole) || packet.roles[0];

  state.activeCopilotRole = activeSummary.role_key;
  copilotTitle.textContent = activeSummary.title;
  copilotStatusPill.textContent = backend ? `${packet.release_status} release` : "Frontend role synthesis";
  copilotStatusPill.dataset.status = backend ? packet.release_status : "loaded";
  copilotSummary.textContent = backend
    ? `${activeSummary.summary} ${packet.explainability_summary}`
    : `${activeSummary.summary} The local prototype keeps the same multi-role structure while backend packets are unavailable.`;

  copilotRoleStrip.innerHTML = packet.roles
    .map(
      (role) => `
        <button
          class="copilot-role-button ${role.role_key === activeSummary.role_key ? "active" : ""}"
          type="button"
          data-copilot-role="${role.role_key}"
          aria-pressed="${String(role.role_key === activeSummary.role_key)}"
        >
          <strong>${role.title}</strong>
          <span>${role.focus}</span>
        </button>
      `
    )
    .join("");

  copilotConversation.innerHTML = packet.conversation
    .map(
      (message) => `
        <div class="message-bubble message-bubble--${message.speaker}">
          <strong>${message.speaker === "assistant" ? message.role : "User"}</strong>
          <p>${message.text}</p>
          <small>Sources • ${message.sources.join(" • ")}</small>
        </div>
      `
    )
    .join("");

  copilotMemoryList.innerHTML = packet.memory
    .map(
      (item) => `
        <div class="stack-item">
          <strong>${item.label}</strong>
          <span>${item.retention}</span>
          <p>${item.value} • Source: ${item.source}</p>
        </div>
      `
    )
    .join("");

  copilotReasoningList.innerHTML = packet.reasoning_trace
    .map(
      (step) => `
        <div class="stack-item">
          <strong>${step.step}</strong>
          <span>${step.experts.join(" • ")}</span>
          <p>${step.detail}</p>
        </div>
      `
    )
    .join("");

  copilotGuardrailList.innerHTML = packet.guardrails
    .map(
      (guardrail) => `
        <div class="stack-item">
          <strong>${guardrail.control}</strong>
          <span>${guardrail.status}</span>
          <p>${guardrail.detail}</p>
        </div>
      `
    )
    .join("");
}

function renderDealBoard() {
  const backend = getBackendSync();
  if (backend?.transaction) {
    const packet = backend.transaction;
    const transaction = packet.transaction;
    const stageInsights = [packet.pricing_strategy, packet.negotiation_insight, packet.document_validation, packet.risk_scoring];

    dealTitle.textContent = transaction.deal_name;
    dealSummary.textContent = packet.explanation;
    dealRiskPill.textContent = packet.risk_rating;
    dealTargetPrice.textContent = currency(transaction.target_price);
    dealCloseWindow.textContent = `${transaction.urgency_days} calendar days`;
    dealIntegrity.textContent = packet.workflow_integrity.sequential_integrity;
    dealContinuity.textContent = packet.workflow_integrity.continuity_mode;

    dealStageList.innerHTML = transaction.workflow_stages
      .map(
        (stage) => `
          <div class="stage-item stage-item--${stage.status.replace(/\s+/g, "-")}">
            <div class="stage-heading">
              <strong>${stage.stage}</strong>
              <span>${stage.status}</span>
            </div>
            <div class="progress-track"><span style="width:${Math.round(stage.completion * 100)}%"></span></div>
            <p>${stage.blocker || stage.control_checks.join(" • ")}</p>
            <small>Owner • ${stage.owner}</small>
          </div>
        `
      )
      .join("");

    dealExpertList.innerHTML = stageInsights
      .map(
        (item) => `
          <div class="stack-item">
            <div class="recommendation-topline">
              <strong>${item.headline}</strong>
              <span>${item.priority} • ${Math.round(item.score * 100)}/100</span>
            </div>
            <p>${item.detail}</p>
          </div>
        `
      )
      .join("");

    documentList.innerHTML = transaction.requested_documents
      .map(
        (document) => `
          <div class="stack-item">
            <div class="recommendation-topline">
              <strong>${document.name}</strong>
              <span>${document.status}</span>
            </div>
            <p>${document.issues.length ? document.issues.join(" • ") : `Document type ${document.document_type}.`}</p>
            <small>Owner • ${document.owner}</small>
          </div>
        `
      )
      .join("");

    complianceControlList.innerHTML = packet.compliance_controls
      .map(
        (control) => `
          <div class="stack-item">
            <div class="recommendation-topline">
              <strong>${control.control}</strong>
              <span>${control.status} • ${control.framework}</span>
            </div>
            <p>${control.detail}</p>
          </div>
        `
      )
      .join("");
    return;
  }

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
  const backend = getBackendSync();
  if (backend?.residency) {
    const packet = backend.residency;
    residencyProgramTitle.textContent = packet.program;
    residencyStatusPill.textContent = packet.eligibility_status;
    residencyStatusPill.dataset.status = packet.eligibility_status.toLowerCase().replace(/\s+/g, "-");
    residencySummary.textContent = packet.explanation;
    eligibilityScore.textContent = `${Math.round(packet.eligibility_score * 100)}/100`;
    pathwayType.textContent = packet.pathway_type;
    kycAmlSummary.textContent = packet.kyc_aml_summary;
    privacySummary.textContent = packet.privacy_summary;
    incomeValue.textContent = `${currency(packet.applicant.annual_income)} household income`;
    assetsValue.textContent = `${currency(packet.applicant.liquid_assets)} liquid assets`;
    propertyValueLabel.textContent = `${currency(packet.applicant.property_value)} property value`;

    ruleCheckList.innerHTML = packet.rule_checks
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

    documentCheckList.innerHTML = packet.document_checks
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

    complianceWorkflowList.innerHTML = packet.compliance_workflow
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
    return;
  }

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
  const backend = getBackendSync();
  if (backend?.insurance) {
    const packet = backend.insurance;
    insuranceProgramTitle.textContent = `${packet.applicant.persona} insurance workspace`;
    insuranceStatusPill.textContent = packet.release_status;
    insuranceStatusPill.dataset.status = packet.release_status.toLowerCase().replace(/\s+/g, "-");
    insuranceSummary.textContent = packet.explanation;
    insuranceReadinessScore.textContent = `${Math.round((packet.recommendations.length / Math.max(packet.acord_coverages.length, 1)) * 100)}/100`;
    insurancePrimaryPackage.textContent = packet.recommendations[0]?.coverage_type || "Coverage review";
    insuranceAcordMode.textContent = packet.secure_exchange_summary;
    insuranceNaicPosture.textContent = packet.naic_privacy_summary;

    insuranceOptionList.innerHTML = packet.recommendations
      .map((item) => `
        <div class="stack-item">
          <div class="recommendation-topline">
            <strong>${item.coverage_type} • ${item.policy_form}</strong>
            <span>${item.recommendation_level} • ${item.premium_estimate}</span>
          </div>
          <p>${item.rationale}</p>
        </div>
      `)
      .join("");

    insurancePayloadList.innerHTML = packet.acord_coverages
      .map((item) => `
        <div class="stack-item">
          <div class="recommendation-topline">
            <strong>${item.coverage_type}</strong>
            <span>${item.acord_form}</span>
          </div>
          <p>${item.notes} • Insured amount ${currency(item.insured_amount)} • Deductible ${currency(item.deductible)}</p>
        </div>
      `)
      .join("");

    insuranceControlList.innerHTML = packet.secure_exchange_controls
      .map((item) => `
        <div class="stack-item">
          <div class="recommendation-topline">
            <strong>${item.control}</strong>
            <span>${item.status}</span>
          </div>
          <p>${item.detail}</p>
        </div>
      `)
      .join("");
    return;
  }

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
  const backend = getBackendSync();
  if (backend?.payment) {
    const packet = backend.payment;
    paymentProgramTitle.textContent = `${packet.payment_instrument.instrument_type} payment orchestration`;
    paymentStatusPill.textContent = packet.risk_level;
    paymentStatusPill.dataset.status = packet.risk_level.toLowerCase().replace(/\s+/g, "-");
    paymentSummary.textContent = packet.explanation;
    paymentAmountValue.textContent = `${currency(packet.payment_instrument.amount || state.paymentAmount)} payment amount`;
    paymentFraudScore.textContent = `${Math.round(packet.fraud_probability * 100)}% probability`;
    paymentBehaviorSummary.textContent = packet.payment_behavior_summary;
    paymentEscrowSummary.textContent = packet.escrow_status;
    paymentFrontendPosture.textContent = packet.frontend_security_posture;

    paymentSignalList.innerHTML = packet.signals
      .map((item) => `
        <div class="stack-item">
          <div class="recommendation-topline">
            <strong>${item.category}</strong>
            <span>${item.status}</span>
          </div>
          <p>${item.detail}</p>
        </div>
      `)
      .join("");

    paymentEscrowList.innerHTML = packet.escrow_conditions
      .map((item) => `
        <div class="stack-item">
          <div class="recommendation-topline">
            <strong>${item.condition}</strong>
            <span>${item.status}</span>
          </div>
          <p>${item.detail}</p>
        </div>
      `)
      .join("");

    paymentReconciliationList.innerHTML = packet.reconciliation_entries
      .map((item) => `
        <div class="stack-item">
          <div class="recommendation-topline">
            <strong>${item.entry_type}</strong>
            <span>${item.status}</span>
          </div>
          <p>${item.detail}</p>
        </div>
      `)
      .join("");
    return;
  }

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

function buildComplianceGraphFallback() {
  const residency = evaluateResidencyProgram();
  const payment = getPaymentScenario();
  const insurance = getInsuranceScenario();
  const activeJurisdictions = ["United States", state.jurisdiction].filter((value, index, array) => array.indexOf(value) === index);
  const overallStatus = payment.fraudProbability >= 0.55 || residency.status !== "Eligible" ? "review" : "active";

  return {
    graph_version: "prototype-local",
    overall_status: overallStatus,
    graph_summary: `The local compliance graph keeps ${activeJurisdictions.join(" → ")} workflows aligned across real estate, payments, insurance, and residency. It adapts release guidance when payment risk, document readiness, or eligibility thresholds change so users understand why a workflow is ready, reviewable, or blocked.`,
    operating_jurisdictions: activeJurisdictions,
    domains: [
      {
        domain: "real_estate",
        jurisdiction: state.jurisdiction,
        workflow_status: state.financing ? "review" : "active",
        regulatory_authorities: ["Transaction counsel", "Municipal registry"],
        guidance_summary: "Property release logic keeps disclosure, financing, and closing-sequence checks visible before the user can move forward.",
        evidence_refs: ["deal controls", "document validation", "release gate"]
      },
      {
        domain: "payments",
        jurisdiction: "United States",
        workflow_status: payment.status === "Release ready" ? "active" : "review",
        regulatory_authorities: ["Escrow operations", "PSP risk desk"],
        guidance_summary: "Payment rules adapt to amount, settlement timing, device trust, and cross-border posture inside the same workflow.",
        evidence_refs: ["fraud score", "escrow conditions", "reconciliation controls"]
      },
      {
        domain: "insurance",
        jurisdiction: state.jurisdiction,
        workflow_status: insurance.status === "Escalate" ? "review" : "active",
        regulatory_authorities: ["Carrier underwriting", "Privacy office"],
        guidance_summary: "Insurance guidance stays transparent about coverage fit, payload requirements, and privacy-scoped exchange controls.",
        evidence_refs: ["coverage stack", "ACORD payload", "NAIC privacy controls"]
      },
      {
        domain: "residency",
        jurisdiction: state.jurisdiction,
        workflow_status: residency.status === "Eligible" ? "active" : "review",
        regulatory_authorities: ["Immigration counsel", "Residency operations"],
        guidance_summary: "Residency rules expose threshold checks, missing documents, and legal review requirements before filing.",
        evidence_refs: ["eligibility score", "document checklist", "workflow steps"]
      }
    ],
    workflow_adaptations: [
      {
        workflow: "property release",
        status: "gated",
        jurisdictions: [state.jurisdiction],
        triggered_by: ["document readiness", "transaction approvals"],
        frontend_guidance: "Show open blockers and next required evidence before offer export or closing release.",
        backend_action: "Keep deal progression behind document and approval controls."
      },
      {
        workflow: "payment release",
        status: payment.status === "Release ready" ? "active" : "adaptive",
        jurisdictions: activeJurisdictions,
        triggered_by: ["fraud probability", "escrow stage", "cross-border posture"],
        frontend_guidance: "Explain in plain language why payment can release now or needs more review.",
        backend_action: "Raise manual-review and dual-approval requirements when risk signals worsen."
      },
      {
        workflow: "insurance exchange",
        status: insurance.status === "Escalate" ? "review" : "active",
        jurisdictions: [state.jurisdiction],
        triggered_by: ["property type", "occupancy", "privacy scope"],
        frontend_guidance: "Clarify which extra coverages or documents are jurisdiction-driven rather than optional upsell.",
        backend_action: "Shape outbound quote payloads according to consent scope and carrier expectations."
      },
      {
        workflow: "residency filing",
        status: residency.status === "Eligible" ? "ready" : "review",
        jurisdictions: [state.jurisdiction],
        triggered_by: ["eligibility rules", "source-of-funds evidence", "health insurance readiness"],
        frontend_guidance: "List every threshold, missing item, and review reason before filing is attempted.",
        backend_action: "Re-score the case whenever evidence or jurisdiction rules change."
      }
    ],
    change_watch: [
      {
        domain: "real_estate",
        jurisdiction: state.jurisdiction,
        impact_level: "Medium",
        change_summary: "Disclosure and filing templates are tracked as versioned policy artifacts.",
        action_required: "Re-run document completeness checks when a new template is detected."
      },
      {
        domain: "payments",
        jurisdiction: "United States",
        impact_level: payment.status === "Release ready" ? "Medium" : "High",
        change_summary: "Cross-border and escrow release policies can tighten without requiring frontend rewrites.",
        action_required: "Escalate manual review when geography, amount, or device trust changes."
      },
      {
        domain: "insurance",
        jurisdiction: state.jurisdiction,
        impact_level: "Medium",
        change_summary: "Carrier intake schemas and privacy notices stay versioned as the exchange model evolves.",
        action_required: "Refresh payload mappings and user guidance when underwriting fields change."
      },
      {
        domain: "residency",
        jurisdiction: state.jurisdiction,
        impact_level: residency.status === "Eligible" ? "Medium" : "High",
        change_summary: "Residency thresholds and filing expectations are treated as a living rule graph.",
        action_required: "Update eligibility scoring and applicant checklists when the program changes."
      }
    ],
    transparency_guidance: [
      {
        title: "User-facing compliance guidance",
        audience: "frontend user",
        summary: "Users should understand which jurisdictional checks affect their workflow and what evidence is still needed.",
        disclosures: [
          "Show active jurisdictions and domain status.",
          "Translate controls into blockers, watch items, and next actions.",
          "Clearly mark policy review as a compliance hold, not an application error."
        ]
      },
      {
        title: "Backend regulatory intelligence guidance",
        audience: "operations and services",
        summary: "Services should consume the graph to adapt release gates, payload shaping, and human review paths.",
        disclosures: [
          "Version policy changes and bind them to audit evidence.",
          "Trigger re-evaluation when regulations or user evidence change.",
          "Limit outbound fields to the active purpose and consent scope."
        ]
      }
    ]
  };
}

function renderComplianceGraph() {
  const backend = getBackendSync();
  const graph = backend?.complianceGraph || buildComplianceGraphFallback();

  complianceGraphTitle.textContent = `${graph.primary_jurisdiction || state.jurisdiction} regulatory intelligence graph`;
  complianceGraphStatus.textContent = graph.overall_status;
  complianceGraphStatus.dataset.status = String(graph.overall_status).toLowerCase().replace(/\s+/g, "-");
  complianceGraphSummary.textContent = graph.graph_summary;
  complianceGraphVersion.textContent = graph.graph_version;
  complianceGraphJurisdictions.textContent = (graph.operating_jurisdictions || []).join(" → ");

  complianceDomainList.innerHTML = (graph.domains || [])
    .map((item) => `
      <div class="stack-item">
        <div class="recommendation-topline">
          <strong>${item.domain.replace(/_/g, " ")}</strong>
          <span>${item.workflow_status} • ${item.jurisdiction}</span>
        </div>
        <p>${item.guidance_summary}</p>
        <small>${(item.regulatory_authorities || []).join(" • ")} • Evidence: ${(item.evidence_refs || []).join(", ")}</small>
      </div>
    `)
    .join("");

  complianceAdaptationList.innerHTML = (graph.workflow_adaptations || [])
    .map((item) => `
      <div class="stack-item">
        <div class="recommendation-topline">
          <strong>${item.workflow}</strong>
          <span>${item.status}</span>
        </div>
        <p>${item.frontend_guidance}</p>
        <small>Triggers • ${(item.triggered_by || []).join(", ")} • Backend • ${item.backend_action}</small>
      </div>
    `)
    .join("");

  complianceChangeList.innerHTML = (graph.change_watch || [])
    .map((item) => `
      <div class="stack-item">
        <div class="recommendation-topline">
          <strong>${item.domain.replace(/_/g, " ")} • ${item.jurisdiction}</strong>
          <span>${item.impact_level}</span>
        </div>
        <p>${item.change_summary}</p>
        <small>Action required • ${item.action_required}</small>
      </div>
    `)
    .join("");

  complianceTransparencyList.innerHTML = (graph.transparency_guidance || [])
    .map((item) => `
      <div class="stack-item">
        <div class="recommendation-topline">
          <strong>${item.title}</strong>
          <span>${item.audience}</span>
        </div>
        <p>${item.summary}</p>
        <small>${(item.disclosures || []).join(" • ")}</small>
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
  const backend = getBackendSync();
  if (backend?.integration) {
    const packet = backend.integration;
    integrationProgramTitle.textContent = packet.partner_system;
    integrationStatusPill.textContent = packet.release_status;
    integrationStatusPill.dataset.status = packet.release_status.toLowerCase().replace(/\s+/g, "-");
    integrationSummary.textContent = packet.explanation;
    integrationCanonicalModel.textContent = packet.canonical_contract;
    integrationExpertChain.textContent = packet.expert_chain.join(" → ");
    integrationSecurityPosture.textContent = packet.validation_results.map((item) => `${item.control}: ${item.status}`).join(" • ");
    integrationRouteTarget.textContent = packet.routing_decisions[0]?.target || "Route pending";

    integrationControlList.innerHTML = packet.validation_results
      .map((item) => `
        <div class="stack-item">
          <div class="recommendation-topline">
            <strong>${item.control}</strong>
            <span>${item.status}</span>
          </div>
          <p>${item.detail}</p>
        </div>
      `)
      .join("");

    integrationRouteList.innerHTML = packet.routing_decisions
      .map((item) => `
        <div class="stack-item">
          <div class="recommendation-topline">
            <strong>${item.target}</strong>
            <span>${item.status}</span>
          </div>
          <p>${item.detail}</p>
        </div>
      `)
      .join("");

    integrationEvidenceList.innerHTML = packet.compliance_evidence
      .map((item, index) => `
        <div class="stack-item">
          <div class="recommendation-topline">
            <strong>Evidence ${index + 1}</strong>
            <span>Attached</span>
          </div>
          <p>${item}</p>
        </div>
      `)
      .join("");
    return;
  }

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

function getTwinScenario() {
  const annualGrossIncome = state.twinMonthlyRent * 12 * state.twinOccupancy;
  const annualOperatingExpenses = annualGrossIncome * state.twinOperatingExpenseRatio + state.twinInsurancePremium;
  const annualNoi = annualGrossIncome - annualOperatingExpenses;
  const annualDebtService = state.budget * state.twinFinancingRatio * state.twinInterestRate;
  const annualCashFlow = annualNoi - annualDebtService;
  const projectedValue = (state.propertyValue + state.twinRenovationBudget * 1.15) * ((1 + state.twinAppreciationRate) ** state.twinHoldYears);
  const baselineEquity = projectedValue - state.budget * state.twinFinancingRatio * 0.92 + annualCashFlow * state.twinHoldYears - state.twinRenovationBudget;
  const reliability = Math.max(0.56, Math.min(0.97, 0.9 - Math.abs(0.92 - state.twinOccupancy) * 0.9 - (state.twinInsurancePremium / 25000) * 0.08 - (state.twinRenovationBudget / 250000) * 0.05));
  const scenarios = [
    {
      title: 'Baseline operating case',
      occupancy: state.twinOccupancy,
      rent: state.twinMonthlyRent,
      insurance: state.twinInsurancePremium,
      annualNoi,
      annualCashFlow,
      projectedValue,
      equity: baselineEquity,
      reliability,
      detail: 'Balances observed occupancy, insurance, and capex assumptions against the active financing plan.'
    },
    {
      title: 'Renovation upside case',
      occupancy: Math.min(0.99, state.twinOccupancy + 0.03),
      rent: state.twinMonthlyRent * 1.08,
      insurance: state.twinInsurancePremium * 1.04,
      annualNoi: annualNoi * 1.13,
      annualCashFlow: annualCashFlow * 1.18,
      projectedValue: projectedValue * 1.09,
      equity: baselineEquity * 1.14,
      reliability: reliability - 0.05,
      detail: 'Assumes renovation lifts rent, occupancy, and exit value but carries additional capex and execution uncertainty.'
    },
    {
      title: 'Insurance and occupancy stress case',
      occupancy: Math.max(0.55, state.twinOccupancy - 0.09),
      rent: state.twinMonthlyRent * 0.96,
      insurance: state.twinInsurancePremium * 1.22,
      annualNoi: annualNoi * 0.82,
      annualCashFlow: annualCashFlow * 0.74,
      projectedValue: projectedValue * 0.93,
      equity: baselineEquity * 0.84,
      reliability: reliability - 0.09,
      detail: 'Tests downside resilience under vacancy, higher premium load, and softer valuation appreciation.'
    }
  ].map((item) => ({
    ...item,
    annualNoi: Math.round(item.annualNoi),
    annualCashFlow: Math.round(item.annualCashFlow),
    projectedValue: Math.round(item.projectedValue),
    equity: Math.round(item.equity),
    reliability: Math.max(0.5, Math.min(0.98, item.reliability))
  }));
  return {
    annualNoi: Math.round(annualNoi),
    annualCashFlow: Math.round(annualCashFlow),
    projectedValue: Math.round(projectedValue),
    reliability,
    scenarios,
    outlook: [
      `Baseline modeled equity outcome is ${currency(Math.round(baselineEquity))} across a ${state.twinHoldYears}-year hold.`,
      `Renovation sensitivity adds a potential ${currency(Math.round(scenarios[1].equity - baselineEquity))} upside if rent and occupancy improve on plan.`,
      `Insurance stress reduces annual cash flow to ${currency(scenarios[2].annualCashFlow)} and highlights the need for resilient coverage planning.`,
      'Every scenario keeps occupancy, renovation, insurance, debt-service, and valuation assumptions visible for challenge and override.'
    ],
    governance: [
      { framework: 'ISO/IEC 42001', status: 'Active', detail: 'Simulation outputs stay under accountable model governance, human review, and release gating.' },
      { framework: 'ISO/IEC 5259', status: 'Active', detail: 'Data quality is visible through explicit variables and reliability scoring rather than opaque predictions.' },
      { framework: 'Explainability', status: 'Active', detail: 'Users can adjust occupancy, rent, insurance, renovation, and hold-period inputs and immediately inspect why results move.' },
      { framework: 'Reliability', status: 'Replayable', detail: 'What-if states are deterministic from the visible inputs, supporting repeatability and operational recovery.' }
    ],
    recommendation: 'Use the twin to decide whether the property still clears cash-flow and equity thresholds after renovation and insurance sensitivity are applied.'
  };
}

function renderDigitalTwinEngine() {
  const backend = getBackendSync();
  const twin = getTwinScenario();
  const backendScenarios = backend?.digitalTwin?.scenarios || [];

  if (backend?.digitalTwin) {
    const packet = backend.digitalTwin;
    twinTitle.textContent = packet.twin.property_name;
    twinStatusPill.textContent = packet.standards_alignment.slice(0, 2).join(' + ');
    twinStatusPill.dataset.status = 'active';
    twinSummary.textContent = `${packet.explanation} ${packet.explainability_summary} Adjust the controls to run an interactive frontend what-if against the governed backend baseline.`;
    twinOutlookList.innerHTML = [
      ...packet.portfolio_outlook,
      packet.recommendation,
      packet.reliability_summary
    ]
      .map((item, index) => `
        <div class="stack-item">
          <div class="recommendation-topline">
            <strong>Outcome ${index + 1}</strong>
            <span>Portfolio view</span>
          </div>
          <p>${item}</p>
        </div>
      `)
      .join('');

    twinGovernanceList.innerHTML = packet.governance_controls
      .map((item) => `
        <div class="stack-item">
          <div class="recommendation-topline">
            <strong>${item.framework}</strong>
            <span>${item.status}</span>
          </div>
          <p><strong>${item.control}.</strong> ${item.detail}</p>
        </div>
      `)
      .join('');
  } else {
    twinTitle.textContent = `${journeys[state.activeJourney].candidates[0].title} twin`;
    twinStatusPill.textContent = 'Interactive what-if';
    twinStatusPill.dataset.status = 'active';
    twinSummary.textContent = `${twin.recommendation} This local simulation blends occupancy, renovation, insurance, financing, and hold-period assumptions into a governed projection.`;
    twinOutlookList.innerHTML = twin.outlook
      .map((item, index) => `
        <div class="stack-item">
          <div class="recommendation-topline">
            <strong>Outcome ${index + 1}</strong>
            <span>Scenario analytics</span>
          </div>
          <p>${item}</p>
        </div>
      `)
      .join('');

    twinGovernanceList.innerHTML = twin.governance
      .map((item) => `
        <div class="stack-item">
          <div class="recommendation-topline">
            <strong>${item.framework}</strong>
            <span>${item.status}</span>
          </div>
          <p>${item.detail}</p>
        </div>
      `)
      .join('');
  }

  twinNoi.textContent = currency(twin.annualNoi);
  twinCashflow.textContent = currency(twin.annualCashFlow);
  twinExitValue.textContent = currency(twin.projectedValue);
  twinReliability.textContent = `${Math.round(twin.reliability * 100)}/100`;
  twinOccupancyValue.textContent = `${Math.round(state.twinOccupancy * 100)}% occupied`;
  twinRentValue.textContent = `${currency(state.twinMonthlyRent)} / month`;
  twinRenovationValue.textContent = `${currency(state.twinRenovationBudget)} capex`;
  twinInsuranceValue.textContent = `${currency(state.twinInsurancePremium)} annual premium`;
  twinHoldValue.textContent = `${state.twinHoldYears} year hold`;

  twinScenarioList.innerHTML = twin.scenarios
    .map((item, index) => {
      const baseline = backendScenarios[index];
      return `
        <div class="stack-item">
          <div class="recommendation-topline">
            <strong>${baseline?.name || item.title}</strong>
            <span>${Math.round(item.reliability * 100)}/100 reliable</span>
          </div>
          <p>${baseline?.explanation || item.detail}</p>
          <small>NOI ${currency(item.annualNoi)} • Cash flow ${currency(item.annualCashFlow)} • Exit ${currency(item.projectedValue)}</small>
        </div>
      `;
    })
    .join('');
}


function getMarketIntelligenceScenario() {
  const profile = marketIntelligenceProfiles[state.activeJourney];
  return {
    ...profile,
    scope: profile.scope,
    signalSummary: profile.signalSummary
  };
}

function renderMarketIntelligenceEngine() {
  const backend = getBackendSync();

  if (backend?.marketIntelligence) {
    const packet = backend.marketIntelligence;
    marketProgramTitle.textContent = packet.market_scope;
    marketStatusPill.textContent = `${packet.forecasts.length} forecasts live`;
    marketStatusPill.dataset.status = 'active';
    marketSummary.textContent = `${packet.explanation} ${packet.recommendation}`;
    marketScope.textContent = packet.market_scope;
    marketHorizon.textContent = `${packet.investment_horizon_months} months`;
    marketStrategyBias.textContent = packet.strategy_bias.replace(/_/g, ' ');
    marketSignalSummary.textContent = packet.signal_summary;

    marketStreamList.innerHTML = packet.data_streams
      .map((item) => `
        <div class="stack-item">
          <div class="recommendation-topline">
            <strong>${item.source}</strong>
            <span>${item.cadence}</span>
          </div>
          <p>${item.coverage}</p>
          <small>${item.freshness_sla} freshness • ${item.features.join(' • ')}</small>
        </div>
      `)
      .join('');

    marketForecastList.innerHTML = [
      ...packet.forecasts.map((item) => ({
        title: item.horizon,
        status: `${Math.round(item.confidence * 100)}/100 confidence`,
        detail: `${item.explanation} Price growth ${(item.price_growth * 100).toFixed(1)}% • Rent growth ${(item.rent_growth * 100).toFixed(1)}% • Cap-rate shift ${item.cap_rate_shift_bps} bps.`,
      })),
      ...packet.alerts.map((item) => ({
        title: item.title,
        status: item.severity,
        detail: `${item.signal} ${item.action}`,
      }))
    ]
      .map((item) => `
        <div class="stack-item">
          <div class="recommendation-topline">
            <strong>${item.title}</strong>
            <span>${item.status}</span>
          </div>
          <p>${item.detail}</p>
        </div>
      `)
      .join('');

    marketPipelineList.innerHTML = packet.pipeline_status
      .map((item) => `
        <div class="stack-item">
          <div class="recommendation-topline">
            <strong>${item.stage}</strong>
            <span>${item.status}</span>
          </div>
          <p>${item.detail}</p>
        </div>
      `)
      .join('');
    return;
  }

  const local = getMarketIntelligenceScenario();
  marketProgramTitle.textContent = local.scope;
  marketStatusPill.textContent = 'Local forecast mode';
  marketStatusPill.dataset.status = 'active';
  marketSummary.textContent = `${local.signalSummary} The backend engine will replace this with governed forecasts, alerts, and ingestion pipeline health once the demo snapshot loads.`;
  marketScope.textContent = local.scope;
  marketHorizon.textContent = local.horizon;
  marketStrategyBias.textContent = local.strategyBias;
  marketSignalSummary.textContent = local.signalSummary;

  marketStreamList.innerHTML = local.streams
    .map((item, index) => `
      <div class="stack-item">
        <div class="recommendation-topline">
          <strong>Stream ${index + 1}</strong>
          <span>Continuous</span>
        </div>
        <p>${item}</p>
      </div>
    `)
    .join('');

  marketForecastList.innerHTML = local.forecasts
    .map((item, index) => `
      <div class="stack-item">
        <div class="recommendation-topline">
          <strong>${index < 2 ? `Forecast ${index + 1}` : 'Alert'}</strong>
          <span>${index < 2 ? 'Outlook' : 'Action'}</span>
        </div>
        <p>${item}</p>
      </div>
    `)
    .join('');

  marketPipelineList.innerHTML = local.pipeline
    .map((item, index) => `
      <div class="stack-item">
        <div class="recommendation-topline">
          <strong>Pipeline stage ${index + 1}</strong>
          <span>Active</span>
        </div>
        <p>${item}</p>
      </div>
    `)
    .join('');
}


function getDocumentIntelligenceScenario() {
  return documentIntelligenceProfiles[state.activeJourney];
}

function renderDocumentIntelligenceEngine() {
  const backend = getBackendSync();

  if (backend?.documentIntelligence) {
    const packet = backend.documentIntelligence;
    documentProgramTitle.textContent = packet.portfolio_name;
    documentStatusPill.textContent = packet.release_status;
    documentStatusPill.dataset.status = packet.release_status.toLowerCase().replace(/\s+/g, "-");
    documentSummary.textContent = `${packet.simplified_summary} ${packet.reasoning_summary}`;
    documentPortfolioName.textContent = packet.portfolio_name;
    documentCount.textContent = `${packet.governed_documents.length} governed docs`;
    documentAnomalySummary.textContent = `${packet.anomaly_signals.length} anomaly signals`;
    documentAuditSummary.textContent = `${packet.audit_records.length} audit events`;

    documentInsightList.innerHTML = packet.frontend_insights
      .map((item, index) => `
        <div class="stack-item">
          <div class="recommendation-topline">
            <strong>Insight ${index + 1}</strong>
            <span>Frontend-safe</span>
          </div>
          <p>${item}</p>
        </div>
      `)
      .join("");

    documentValidationList.innerHTML = [
      ...packet.extracted_fields.map((item) => ({
        title: `${item.field_name.replace(/_/g, " ")}`,
        status: `${Math.round(item.confidence * 100)}/100 confidence`,
        detail: `${item.field_value} • Normalized ${item.normalized_value}. ${item.rationale}`
      })),
      ...packet.validation_checks.map((item) => ({
        title: item.check_name,
        status: `${item.status} • ${item.severity}`,
        detail: item.detail
      }))
    ]
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

    documentGovernanceList.innerHTML = [
      ...packet.anomaly_signals.map((item) => ({
        title: item.signal,
        status: item.severity,
        detail: `${item.detail} ${item.recommended_action}`
      })),
      ...packet.compliance_findings.map((item) => ({
        title: `${item.framework} • ${item.control}`,
        status: item.status,
        detail: item.detail
      })),
      ...packet.audit_records.map((item) => ({
        title: `${item.event.replace(/_/g, " ")}`,
        status: item.actor,
        detail: item.detail
      }))
    ]
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
    return;
  }

  const local = getDocumentIntelligenceScenario();
  documentProgramTitle.textContent = local.portfolioName;
  documentStatusPill.textContent = local.status;
  documentStatusPill.dataset.status = "active";
  documentSummary.textContent = local.summary;
  documentPortfolioName.textContent = local.portfolioName;
  documentCount.textContent = `${local.documents} governed docs`;
  documentAnomalySummary.textContent = "Medium review";
  documentAuditSummary.textContent = "4 audit events";

  documentInsightList.innerHTML = local.insights
    .map((item, index) => `
      <div class="stack-item">
        <div class="recommendation-topline">
          <strong>Insight ${index + 1}</strong>
          <span>Frontend-safe</span>
        </div>
        <p>${item}</p>
      </div>
    `)
    .join("");

  documentValidationList.innerHTML = local.validation
    .map((item, index) => `
      <div class="stack-item">
        <div class="recommendation-topline">
          <strong>Validation ${index + 1}</strong>
          <span>Explainable check</span>
        </div>
        <p>${item}</p>
      </div>
    `)
    .join("");

  documentGovernanceList.innerHTML = local.governance
    .map((item, index) => `
      <div class="stack-item">
        <div class="recommendation-topline">
          <strong>Governance ${index + 1}</strong>
          <span>Backend control</span>
        </div>
        <p>${item}</p>
      </div>
    `)
    .join("");
}


function renderNextActions(journey, topCandidate) {
  const backend = getBackendSync();
  if (backend) {
    const dynamicActions = [
      ...backend.property.expert_outputs.slice(0, 3).flatMap((item) => item.next_actions),
      ...backend.transaction.recommendations.slice(0, 2),
      ...backend.payment.recommended_actions.slice(0, 2)
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
    return;
  }

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
  renderWiringStatus();
  const journey = journeys[state.activeJourney];
  const rankedCandidates = rankCandidates();
  const topCandidate = rankedCandidates[0];
  const backend = getBackendSync();
  const backendTopCandidate = backend?.property?.ranked_recommendations?.[0];

  title.textContent = journey.title;
  summary.textContent = backend?.property?.explanation || journey.summary;
  confidence.textContent = backendTopCandidate ? backendTopCandidate.confidence.toFixed(2) : topCandidate.aggregateScore.toFixed(2);
  releaseStatus.textContent = backend?.property?.release_status || getReleaseTone();
  headline.textContent = backend?.property?.recommendation || journey.headline;
  subtitle.textContent = backend
    ? `Backend snapshot verified for ${backend.property.profile.country} → ${backend.property.profile.target_region} with ${backend.property.selected_experts.length} experts and ${backend.property.policy_gates.length} policy gates.`
    : journey.subtitle;
  investorType.textContent = backend?.property?.profile?.investor_type?.replace(/_/g, " ") || journey.profile.investorType;
  locationValue.textContent = backend ? `${backend.property.profile.country} → ${backend.property.profile.target_region}` : journey.profile.location;
  financialIntent.textContent = backend?.property?.profile?.financial_intent || journey.profile.financialIntent;
  residencyGoal.textContent = backend ? backend.property.profile.residency_goal : state.residency ? journey.profile.residencyGoal : "Not currently prioritized";
  accessState.textContent = backend
    ? `${backend.property.identity.rbac_roles.join(" / ")} • ${backend.property.identity.mfa_completed ? "MFA complete" : "MFA pending"}`
    : journey.profile.access;

  action.textContent = backend?.transaction?.recommendations?.[0] || buildActionText(topCandidate);
  risk.textContent = backend
    ? `${backend.property.expert_outputs[0].summary} Transaction risk is ${backend.transaction.risk_rating} and payment risk is ${backend.payment.risk_level}.`
    : buildRiskText(topCandidate);
  why.textContent = backendTopCandidate?.why || buildWhyText(topCandidate);

  steps.innerHTML = backend
    ? [
        `Detected intents: ${backend.property.detected_intents.join(", ")}.`,
        `Top recommendation: ${backendTopCandidate.title} in ${backendTopCandidate.geography}.`,
        `Transaction release is ${backend.transaction.release_status} with ${backend.transaction.compliance_controls.length} tracked controls.`,
        `Residency, insurance, payment, integration, digital twin, market intelligence, document intelligence, and tokenization design surfaces rendered from backend packets or governed frontend content.`
      ]
        .map((item) => `<li>${item}</li>`)
        .join("")
    : journey.steps.map((item) => `<li>${item}</li>`).join("");

  if (backend) {
    expertStrip.innerHTML = backend.property.selected_experts
      .slice(0, 6)
      .map((item) => `<span class="expert-pill">🧠 ${item.expert.replace(/_/g, " ")} ${Math.round(item.score * 100)}%</span>`)
      .join("");
  } else {
    const weights = buildWeights();
    expertStrip.innerHTML = Object.entries(weights)
      .sort((a, b) => b[1] - a[1])
      .map(([key, value]) => `<span class="expert-pill">${expertMeta[key].icon} ${Math.round(value * 100)}%</span>`)
      .join("");
  }

  renderPropertyList(rankedCandidates);
  renderInsights(rankedCandidates);
  renderValuation(rankedCandidates);
  renderGovernance();
  renderContributions(topCandidate);
  renderCopilot(journey, topCandidate);
  renderDealBoard();
  renderDigitalTwinEngine();
  renderMarketIntelligenceEngine();
  renderDocumentIntelligenceEngine();
  renderResidencyEngine();
  renderComplianceGraph();
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

copilotRoleStrip.addEventListener("click", (event) => {
  const button = event.target.closest("[data-copilot-role]");
  if (!button) return;
  state.activeCopilotRole = button.dataset.copilotRole;
  renderJourney();
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

twinOccupancyRange.addEventListener("input", (event) => {
  state.twinOccupancy = Number(event.target.value);
  renderJourney();
});

twinRentRange.addEventListener("input", (event) => {
  state.twinMonthlyRent = Number(event.target.value);
  renderJourney();
});

twinRenovationRange.addEventListener("input", (event) => {
  state.twinRenovationBudget = Number(event.target.value);
  renderJourney();
});

twinInsuranceRange.addEventListener("input", (event) => {
  state.twinInsurancePremium = Number(event.target.value);
  renderJourney();
});

twinHoldRange.addEventListener("input", (event) => {
  state.twinHoldYears = Number(event.target.value);
  renderJourney();
});

async function initializeApp() {
  populateStaticControls();
  applyJourneyDefaults("buyer");
  renderJourney();
  await loadBackendSnapshot();
  renderJourney();
}

initializeApp();
