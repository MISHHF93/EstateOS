const journeys = {
  buyer: {
    title: "Buyer journey",
    confidence: "0.93",
    steps: [
      "Capture investor type, current residence, financial intent, and residency goals from the frontend trust form.",
      "Bind consent scope, MFA state, and KYC posture to the session before expert routing begins.",
      "Shortlist properties using location, amenities, commute, lifestyle, and financing constraints.",
      "Release recommendations only after RBAC, sanctions, privacy, and affordability checks pass."
    ],
    action:
      "Prioritize a Lisbon mixed-use apartment with green retrofit potential, then launch pre-qualification, RBI eligibility review, and bundled insurance intake in a guided next step.",
    risk:
      "Overall posture is controlled. Identity is verified, MFA is active for export actions, and no sanctions blockers are present. The system still recommends enhanced source-of-funds evidence because the residency pathway is cross-border.",
    why:
      "The orchestrator used buyer intent plus frontend-captured profile signals to activate property, finance, insurance, RBI, and compliance experts. Response detail is restricted to the user's entitlements and privacy tier so the recommendation remains personalized without exposing unnecessary data.",
    experts: ["Property", "Pricing", "Compliance", "Finance", "Insurance", "RBI"],
    profile: {
      investorType: "Owner-occupier",
      location: "United States → Portugal",
      financialIntent: "Primary residence with moderate appreciation",
      residencyGoal: "Family relocation in 12 months",
      access: "Client RBAC • MFA on release"
    }
  },
  investor: {
    title: "Investor journey",
    confidence: "0.91",
    steps: [
      "Model investor category, target returns, leverage limits, hold period, and allowed jurisdictions.",
      "Route profile, consent, KYC state, AML risk, and sanctions status into the MoE router.",
      "Evaluate projected yield, vacancy resilience, currency volatility, and RBI fit across markets.",
      "Apply step-up MFA, suitability, concentration, and policy release checks before recommendations are published."
    ],
    action:
      "Advance a diversified shortlist of residential assets in Dubai and Athens, with staggered capital deployment and jurisdiction-specific RBI documentation pathways.",
    risk:
      "Posture is moderate. Yield outlook is attractive, but the system flags FX sensitivity, policy-change risk, and medium AML risk. The recommendation therefore remains reviewable by an advisor before any partner-facing export occurs.",
    why:
      "The router elevated pricing, finance, RBI, and compliance experts after detecting a cross-border investment objective, residency intent, and institutional-style return goals. RBAC and privacy controls permit full portfolio analysis for this user while still masking raw KYC evidence from non-compliance roles.",
    experts: ["Pricing", "Finance", "RBI", "Risk", "Compliance"],
    profile: {
      investorType: "Cross-border investor",
      location: "United States → UAE / Greece",
      financialIntent: "Income plus long-term appreciation",
      residencyGoal: "Optional second residency",
      access: "Investor RBAC • MFA on export"
    }
  },
  advisor: {
    title: "Advisor console",
    confidence: "0.96",
    steps: [
      "Inspect the client profile payload, consent receipt, sanctions result, and expert outputs in one evidence panel.",
      "Confirm role entitlements and enforce step-up MFA before approving or exporting recommendations.",
      "Compare expert recommendations, confidence bands, and policy gate outcomes.",
      "Approve, request more evidence, or hold the package with a complete audit trail."
    ],
    action:
      "Review the composite recommendation, approve the compliance-cleared option, and issue a client-ready memo with assumptions, sensitivity ranges, and insurer-ready intake data.",
    risk:
      "Posture is strong. All critical policy checks passed, the explanation ledger is complete, and only low-severity documentation follow-ups remain. Separation-of-duties controls prevent the same user from both clearing compliance and overriding sanctions outcomes.",
    why:
      "The advisor experience emphasizes transparent control over opaque automation. EstateOS surfaces expert contributions, evidence provenance, trust posture, and policy versions so humans can challenge or endorse AI output with full context and compliant release scope.",
    experts: ["All experts", "Identity trust", "Policy gate", "Human review"],
    profile: {
      investorType: "Advisor-managed portfolio",
      location: "Global client coverage",
      financialIntent: "Suitability and portfolio oversight",
      residencyGoal: "Jurisdiction-specific advisory",
      access: "Advisor RBAC • Entitled approval"
    }
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
const investorType = document.getElementById("profile-investor-type");
const locationValue = document.getElementById("profile-location");
const financialIntent = document.getElementById("profile-financial-intent");
const residencyGoal = document.getElementById("profile-residency-goal");
const accessState = document.getElementById("profile-access-state");

function renderJourney(key) {
  const journey = journeys[key];
  title.textContent = journey.title;
  confidence.textContent = journey.confidence;
  action.textContent = journey.action;
  risk.textContent = journey.risk;
  why.textContent = journey.why;
  investorType.textContent = journey.profile.investorType;
  locationValue.textContent = journey.profile.location;
  financialIntent.textContent = journey.profile.financialIntent;
  residencyGoal.textContent = journey.profile.residencyGoal;
  accessState.textContent = journey.profile.access;

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
