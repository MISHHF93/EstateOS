const journeys = {
  buyer: {
    title: "Buyer journey",
    summary: "Balanced recommendations for livability, affordability, relocation readiness, and low-friction next steps.",
    confidence: 0.93,
    releaseStatus: "Ready to release",
    headline: "Personalized shortlist shaped by property, finance, visa, insurance, and compliance experts",
    subtitle: "The system favors clarity first, then surfaces deeper evidence as the user asks for it.",
    steps: [
      "Capture investor type, relocation timeline, budget, and privacy preferences from the adaptive intake panel.",
      "Route the request through property, finance, visa, insurance, and compliance experts based on stated goals.",
      "Rank candidate properties by fit, risk, residency alignment, and insurability instead of price alone.",
      "Release only policy-cleared recommendations with clear reasons, evidence, and next-best actions."
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
    ]
  },
  investor: {
    title: "Investor journey",
    summary: "Ranked opportunities optimized for yield, resilience, optional residency pathways, and transparent downside analysis.",
    confidence: 0.91,
    releaseStatus: "Reviewable with advisor",
    headline: "Portfolio-style comparison that blends return, jurisdiction, and insurability signals",
    subtitle: "Investors get richer scenario framing and sensitivity awareness than consumer buyers.",
    steps: [
      "Capture return goals, hold period, cross-border intent, and diversification preferences.",
      "Aggregate investment, pricing, visa, insurance, finance, and compliance outputs into one ranking model.",
      "Explain which expert signals lifted or lowered each candidate instead of presenting a black-box score.",
      "Escalate medium-risk cases to advisor review before export or partner actions."
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
    ]
  },
  advisor: {
    title: "Advisor console",
    summary: "Evidence-first oversight that exposes ranking logic, policy outcomes, and release-ready client guidance.",
    confidence: 0.96,
    releaseStatus: "Approval-ready",
    headline: "Advisor view optimized for challenge, endorsement, and documented human oversight",
    subtitle: "The workspace expands explanation depth and surfaces evidence and gating status by default.",
    steps: [
      "Inspect profile context, policy posture, and expert outputs in a single evidence panel.",
      "Compare ranked property options and supporting visa, finance, and insurance narratives side by side.",
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
    ]
  }
};

const expertMeta = {
  property: { label: "Property expert", icon: "Property" },
  investment: { label: "Investment expert", icon: "Investment" },
  visa: { label: "Visa expert", icon: "Visa" },
  insurance: { label: "Insurance expert", icon: "Insurance" },
  finance: { label: "Finance expert", icon: "Finance" },
  compliance: { label: "Compliance expert", icon: "Compliance" },
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

const governanceProfiles = [
  {
    framework: "ISO/IEC 5259",
    title: "Data quality governance",
    summary: "Market feeds, comparables, trend signals, and location intelligence are tested for freshness, completeness, and provenance.",
    controls: "Freshness SLAs • Comparable coverage • Feature provenance • Remediation logging"
  },
  {
    framework: "ISO/IEC 42001",
    title: "AI management governance",
    summary: "Valuation and recommendation models are managed with accountable ownership, fairness reviews, explainability, and human oversight triggers.",
    controls: "Model inventory • Human review • Fairness checks • Explainability ledger"
  }
];

const state = {
  activeJourney: "buyer",
  objective: "relocate",
  risk: "balanced",
  explanationDepth: "guided",
  budget: 650000,
  residency: true,
  financing: true
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
  populateObjectives();
  objectiveSelect.value = state.objective;
}

function populateObjectives() {
  const options = journeys[state.activeJourney].objectives;
  objectiveSelect.innerHTML = options
    .map((option) => `<option value="${option.value}">${option.label}</option>`)
    .join("");
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
  const weightedScore = Object.entries(enrichedExperts).reduce((sum, [expert, expertScore]) => {
    return sum + expertScore * weights[expert];
  }, 0);

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
    return `${topCandidate.title} leads because ${sortedContributors.join(", ")} align best with the current goals, budget, and trust posture.`;
  }

  return `${topCandidate.title} leads because the ${sortedContributors[0]} contributed most to the composite score, while budget fit, ${
    state.residency ? "residency eligibility, " : ""
  }and ${state.financing ? "financing readiness" : "compliance confidence"} remained stronger than the alternatives.`;
}

function buildRiskText(topCandidate) {
  const budgetDelta = state.budget - topCandidate.price;
  const budgetText = budgetDelta >= 0 ? `within budget by ${currency(budgetDelta)}` : `above budget by ${currency(Math.abs(budgetDelta))}`;
  const intelligence = getIntelligence(topCandidate);
  return `${topCandidate.insurance.summary} ${intelligence.trend} The current recommendation is ${budgetText}, climate risk is ${topCandidate.climateRisk}, and release posture is ${getReleaseTone().toLowerCase()}.`;
}

function buildActionText(topCandidate) {
  if (state.activeJourney === "advisor") {
    return `Prepare a client memo for ${topCandidate.title}, confirm policy evidence, and use the explanation ledger to justify why it outranks the rest of the shortlist.`;
  }
  if (state.activeJourney === "investor") {
    return `Advance ${topCandidate.title} into diligence, then compare downside resilience, optional residency steps, and insurance carry before capital is committed.`;
  }
  return `Prioritize ${topCandidate.title}, move into financing and residency planning, and keep the insurance package bundled to reduce friction for the household.`;
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
    .map((profile) => `
      <div class="stack-item">
        <strong>${profile.framework} • ${profile.title}</strong>
        <span>${profile.controls}</span>
        <p>${profile.summary}</p>
      </div>
    `)
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

function renderNextActions(journey, topCandidate) {
  const dynamicActions = [
    ...journey.nextActions,
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

populateStaticControls();
applyJourneyDefaults("buyer");
renderJourney();
