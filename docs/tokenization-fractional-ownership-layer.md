# Tokenization & Fractional Ownership Layer

The Tokenization & Fractional Ownership Layer is a Phase 3 capability that allows EstateOS to support compliant, auditable investment into fractional real-estate interests. The goal is not to reduce property ownership into a simple “buy token” widget. The goal is to let the frontend present a governed investment experience while the backend preserves the legal wrapper, cap-table integrity, transfer controls, payment settlement, and compliance evidence required for real asset ownership.

## 1. Purpose

This layer allows EstateOS to:

- package an eligible property or property-holding entity into a legally defined investment vehicle,
- expose a compliant frontend flow where investors can review an offering and subscribe to fractional interests,
- maintain the authoritative ownership ledger and beneficial-owner records,
- enforce KYC, AML, sanctions, accreditation, suitability, and jurisdiction-specific transfer restrictions,
- reconcile subscriptions, cash movements, distributions, redemptions, and secondary transfers,
- produce evidence suitable for auditors, administrators, legal counsel, and regulators.

## 2. Product outcome

The frontend should be able to present:

- property-backed offerings with unit economics, minimum ticket size, expected cash-yield ranges, lock-up terms, and risk disclosures,
- investor onboarding steps for identity verification, investor classification, suitability, and source-of-funds checks,
- a subscription flow that captures reservations, signed disclosures, wallet or custody preferences, and payment instructions,
- ownership dashboards that show subscribed units, distributions, pending transfers, governance rights, and document history,
- transfer and redemption requests with clear explanations of any lock-up, whitelist, or jurisdictional restriction,
- explainable compliance and settlement status so users understand why an order is approved, held, or rejected.

## 3. Operating model

EstateOS should treat tokenization as a governed asset-administration workflow rather than a standalone blockchain feature.

### 3.1 Core principle

The **legal cap table remains authoritative**, while digital tokens act as the programmable representation of the investor interest inside allowed operational boundaries.

This means:

1. a property is first placed into a legal ownership wrapper such as an SPV, trust, fund, or nominee structure,
2. the rights represented by the digital units are mapped to offering documents and governing agreements,
3. every mint, transfer, lock, burn, pledge, or distribution event must reconcile against the legal ownership ledger,
4. no token movement is considered final unless compliance, settlement, and registry synchronization all succeed.

### 3.2 Trust boundaries

The platform should distinguish clearly between:

- **Legal ownership system of record**: cap table, beneficial owners, investor rights, voting rights, liens, and regulatory filings.
- **Digital token ledger**: token balances, wallet/custody references, transfer-state, smart-contract events, and settlement hooks.
- **Cash and payment ledger**: subscription funds, escrow status, distribution payments, fees, taxes, and reconciliation references.
- **Compliance evidence ledger**: KYC packets, AML decisions, accreditation proof, disclosures, approvals, sanctions results, and audit evidence.

## 4. Frontend experience design

### 4.1 Offering marketplace

The investor workspace should show:

- offering status,
- asset structure and domicile,
- price per unit and minimum commitment,
- investor eligibility gates,
- expected distribution cadence,
- lock-up period,
- transfer policy,
- primary risk disclosures.

### 4.2 Subscription journey

A typical frontend subscription flow should include:

1. review asset summary and legal wrapper,
2. review PPM / offering memorandum / disclosures,
3. complete investor classification and suitability intake,
4. complete KYC/AML and beneficial-owner attestations,
5. reserve units,
6. bind signature and consent records,
7. initiate payment and escrow settlement,
8. receive minted or allocated units only after final settlement and policy clearance.

### 4.3 Ownership workspace

After investment, the frontend should support:

- current holdings,
- distribution history,
- pending corporate actions,
- transfer eligibility,
- tax-document availability,
- voting or governance notices,
- immutable transaction history and downloadable evidence packets.

## 5. Backend service responsibilities

### 5.1 Tokenization domain service

A dedicated tokenization module or service should manage:

- asset eligibility for fractionalization,
- offering creation and lifecycle state,
- unit supply configuration,
- mint / allocation / lock / burn instructions,
- investor positions,
- corporate actions,
- secondary transfer workflows,
- synchronization with legal and financial ledgers.

### 5.2 Supporting services

The layer should coordinate with:

- `services/compliance-service` for KYC/AML/sanctions/PEP, accreditation, suitability, and beneficial-ownership checks,
- `services/payment-service` for subscription funds, escrow release, distributions, redemptions, and reconciliation,
- `services/transaction-service` for property acquisition/holding events and asset-level milestones,
- `services/document-service` for offering documents, disclosures, signatures, tax forms, and evidence packages,
- `services/integration-service` for custodians, fund administrators, registrars, transfer agents, banks, and regulatory reporting adapters,
- `services/admin-reporting-service` for cap-table reporting, investor statements, exception queues, and regulator-ready exports,
- `services/ai-orchestrator` for policy-aware explanations, investor guidance, and anomaly detection.

## 6. Canonical data model

The backend should maintain at least the following governed entities:

### 6.1 Asset wrapper

- asset / property ID,
- legal wrapper type,
- domicile and governing law,
- valuation basis,
- supply cap,
- minimum investment,
- sponsor allocation,
- retail or qualified-investor allocation,
- transfer restrictions,
- offering status.

### 6.2 Investor position

- investor subject ID,
- beneficial-owner record,
- investor class,
- wallet or custody account reference,
- subscribed units,
- settled units,
- lock-up state,
- voting rights,
- distribution preferences,
- tax and withholding profile.

### 6.3 Transaction ledger

- reservation,
- subscription,
- payment authorization,
- escrow settlement,
- mint / allocation,
- transfer,
- distribution,
- redemption,
- cancellation,
- exception and reversal events.

### 6.4 Compliance evidence

- KYC status,
- AML risk score,
- sanctions result,
- accreditation or suitability outcome,
- source-of-funds evidence,
- disclosure acceptance,
- jurisdiction eligibility,
- transfer review outcome.

## 7. Compliance and legal design

The tokenization layer should be designed to fit conventional financial-control expectations even when blockchain infrastructure is used.

### 7.1 Required control themes

- investor identity verification and beneficial-owner traceability,
- AML, sanctions, and PEP screening,
- accreditation / suitability / appropriateness checks where required,
- securities-law and offering-exemption mapping by jurisdiction,
- transfer-agent style controls and whitelist enforcement,
- segregation of duties between issuance, compliance override, and fund release,
- tamper-evident audit trails for ownership and payment events,
- clear disclosure of legal rights, redemption rights, lock-ups, and transfer limits.

### 7.2 Regulatory framework alignment

The design should remain compatible with:

- securities-law compliance in each target jurisdiction,
- KYC / AML / sanctions / beneficial ownership obligations,
- SOC 2 Type 2 and ISO/IEC 27001 logging and access controls,
- ISO/IEC 27701 privacy controls for investor data,
- PCI DSS boundaries for subscription and distribution payments,
- financial-record retention and regulator-review expectations.

## 8. Settlement and transfer lifecycle

### 8.1 Primary issuance

1. asset wrapper is created and approved,
2. offering documents are versioned and released,
3. investor is cleared for the specific offering,
4. reservation is accepted,
5. funds are received and reconciled,
6. issuance engine allocates or mints units,
7. legal ledger and digital ledger are reconciled,
8. investor receives a final ownership confirmation.

### 8.2 Secondary transfer

A transfer should pass through:

- seller eligibility check,
- buyer KYC / suitability approval,
- lock-up and whitelist enforcement,
- price and quantity validation,
- settlement confirmation,
- cap-table and token-ledger synchronization,
- regulator/reporting evidence capture.

### 8.3 Distributions and redemptions

Distributions should be governed like any other financial movement:

- payable amount calculation,
- entitlement snapshot,
- withholding/tax handling,
- payout orchestration,
- reconciliation,
- investor statement generation,
- exception handling for failed or returned funds.

## 9. Auditability requirements

Every tokenization event should preserve:

- actor,
- authority basis,
- policy version,
- legal entity and asset context,
- compliance result IDs,
- payment references,
- smart-contract or ledger references,
- before/after balances,
- timestamps,
- linked documents and approvals.

The platform should support replayable evidence packs for internal audit, external audit, regulator review, and dispute handling.

## 10. AI-assisted controls

The AI layer can assist with:

- offering summarization and investor Q&A,
- transfer anomaly detection,
- suspicious subscription pattern detection,
- disclosure completeness checks,
- jurisdiction-aware compliance explanations,
- reconciliation exception triage,
- shareholder communications drafting.

It should **not** be allowed to bypass issuance controls, alter ownership rights, or finalize transfers without policy-approved workflows.

## 11. Suggested backend packet contract

The frontend-facing tokenization packet should expose:

- asset wrapper summary,
- offering metrics,
- compliance-gate results,
- ownership ledger snapshots,
- transaction and distribution ledger events,
- transfer policy summary,
- release status,
- explainability summary,
- standards and control alignment references.

## 12. Repository mapping

The current reference implementation for this design should live in:

- `docs/tokenization-fractional-ownership-layer.md` for the architecture and operating model,
- `backend/orchestration.py` for the demo packet model and governed issuance/ownership example,
- `backend/api_contract.json` for the public contract expectations,
- `frontend/` for the investor-facing tokenization and fractional ownership prototype,
- `scripts/export_demo_payloads.py` for the generated static snapshot consumed by the prototype.
