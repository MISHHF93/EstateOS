const journeys = {
  buyer: {
    title: "Buyer journey",
    confidence: "0.91",
    steps: [
      "Capture intent, budget, household profile, and target jurisdictions.",
      "Shortlist properties using location, amenities, commute, lifestyle, and financing constraints.",
      "Blend pricing, insurance, and residency insights into a single recommendation.",
      "Run identity, sanctions, privacy, and affordability checks before action release."
    ],
    action:
      "Prioritize a Lisbon mixed-use apartment with green retrofit potential, then launch pre-qualification, RBI eligibility review, and bundled insurance intake in a guided next step.",
    risk:
      "Overall posture is controlled. Climate exposure is moderate, affordability passes base and stressed scenarios, and no sanctions or KYC blockers are detected. The system recommends enhanced document verification for cross-border source-of-funds evidence.",
    why:
      "The orchestrator selected property discovery, pricing, compliance, finance, insurance, and RBI experts because the user expressed both owner-occupier and residency objectives. Confidence increased because the selected asset satisfies budget, livability, financing, and migration thresholds simultaneously.",
    experts: ["Property", "Pricing", "Compliance", "Finance", "Insurance", "RBI"]
  },
  investor: {
    title: "Investor journey",
    confidence: "0.88",
    steps: [
      "Model target returns, leverage limits, hold period, and acceptable jurisdictions.",
      "Evaluate projected yield, vacancy resilience, currency and policy volatility, and exit scenarios.",
      "Assess residency-by-investment pathways that align with capital allocation strategy.",
      "Apply sanctions, AML, suitability, and concentration checks before recommendation release."
    ],
    action:
      "Advance a diversified shortlist of residential assets in Dubai and Athens, with staggered capital deployment and jurisdiction-specific RBI documentation pathways.",
    risk:
      "Posture is moderate. Yield outlook is attractive, but the system flags FX sensitivity and local policy change risk. The recommendation includes hedging review, enhanced legal diligence, and concentration caps before commitment.",
    why:
      "The router elevated pricing, finance, RBI, and risk experts after detecting a cross-border investment objective with multiple regulatory implications. The recommendation favors diversification because return targets can be met without overexposure to any single jurisdiction or asset class.",
    experts: ["Pricing", "Finance", "RBI", "Risk", "Compliance"]
  },
  advisor: {
    title: "Advisor console",
    confidence: "0.94",
    steps: [
      "Inspect user narrative, source documents, and model outputs in a unified evidence panel.",
      "Compare expert recommendations, confidence bands, and policy gate outcomes.",
      "Apply human override, request more evidence, or approve the recommendation package.",
      "Export the audit-ready rationale to client, committee, or insurer stakeholders."
    ],
    action:
      "Review the composite recommendation, approve the compliance-cleared option, and issue a client-ready memo with assumptions, sensitivity ranges, and insurer-ready intake data.",
    risk:
      "Posture is strong. All critical policy checks passed, the explanation ledger is complete, and the system identifies only low-severity documentation follow-ups. Human override remains available for exceptional circumstances.",
    why:
      "The advisor experience emphasizes transparency over automation. EstateOS surfaces expert contributions, evidence provenance, and policy versions so humans can challenge or endorse AI output with a complete, traceable context.",
    experts: ["All experts", "Audit ledger", "Policy gate", "Human review"]
  }
};

const title = document.getElementById("journey-title");
const confidence = document.getElementById("journey-confidence");
const steps = document.getElementById("journey-steps");
const action = document.getElementById("journey-action");
const risk = document.getElementById("journey-risk");
const why = document.getElementById("journey-why");
const expertStrip = document.getElementById("expert-strip");
const cards = document.querySelectorAll(".journey-card");

function renderJourney(key) {
  const journey = journeys[key];
  title.textContent = journey.title;
  confidence.textContent = journey.confidence;
  action.textContent = journey.action;
  risk.textContent = journey.risk;
  why.textContent = journey.why;

  steps.innerHTML = "";
  journey.steps.forEach((item) => {
    const li = document.createElement("li");
    li.textContent = item;
    steps.appendChild(li);
  });

  expertStrip.innerHTML = "";
  journey.experts.forEach((expert) => {
    const span = document.createElement("span");
    span.className = "expert-pill";
    span.textContent = expert;
    expertStrip.appendChild(span);
  });

  cards.forEach((card) => {
    card.classList.toggle("active", card.dataset.journey === key);
  });
}

cards.forEach((card) => {
  card.addEventListener("click", () => renderJourney(card.dataset.journey));
});

renderJourney("buyer");
