# Advanced Document Intelligence & Legal AI

The Advanced Document Intelligence & Legal AI capability is a Phase 3 EstateOS layer for extracting, validating, summarizing, and reasoning over contracts, title packets, insurance policies, and immigration evidence. The goal is not simply to OCR documents. The goal is to let the frontend show simplified, trustworthy insights while the backend remains authoritative for parsing quality, anomaly detection, compliance checks, legal reasoning boundaries, and full auditability.

## 1. Purpose

This capability allows EstateOS to:

- ingest heterogeneous real-estate, insurance, and migration documents into a governed backend workflow,
- extract high-value legal, financial, and identity fields with confidence scores and normalization metadata,
- validate completeness, consistency, and release readiness across multiple document types,
- summarize document meaning into plain-language frontend insights without exposing raw sensitive evidence,
- detect anomalies such as missing clauses, inconsistent dates, mismatched values, and unresolved dependencies,
- preserve complete audit trails for legal, compliance, operations, and regulator review.

## 2. Product outcome

The frontend should be able to present:

- document-specific summaries for contracts, title reports, insurance packets, and immigration files,
- plain-language explanations of what each document means for the active deal or filing,
- confidence-backed extraction results for critical fields such as purchase price, insured amount, title status, and pathway type,
- clear warnings when evidence is missing, conflicting, expired, or blocked for release,
- simplified next steps for buyers, investors, advisors, and operators.

The backend should remain responsible for:

- ingestion provenance and file-hash tracking,
- extraction and normalization quality controls,
- cross-document validation and anomaly detection,
- privacy-tier enforcement and role-aware release shaping,
- immutable audit logging and regulator-ready evidence reconstruction.

## 3. Scope of documents

The first governed document families should include:

1. **Contracts**
   - purchase agreements,
   - amendments,
   - seller disclosures,
   - addenda,
   - signatures and approvals.
2. **Title and property records**
   - title reports,
   - encumbrance extracts,
   - registry certificates,
   - permit and zoning evidence,
   - ownership-chain records.
3. **Insurance documents**
   - quotes,
   - binders,
   - policy schedules,
   - endorsements,
   - claims or underwriting evidence where relevant.
4. **Immigration and residency evidence**
   - passports,
   - proof-of-funds,
   - criminal-record certificates,
   - health-insurance evidence,
   - residency filing packets and supporting attachments.

## 4. Core backend workflow

### 4.1 Ingestion

Each file should be registered with:

- document type,
- source system,
- jurisdiction,
- language,
- upload or connector provenance,
- cryptographic hash,
- correlation to a deal, filing, or investor profile.

### 4.2 Extraction

The extraction pipeline should produce:

- raw text or structural parse output,
- normalized fields,
- field-level confidence,
- rationale or evidence snippets,
- versioned extraction metadata,
- reprocessing status if the parser or policy changes.

### 4.3 Validation

Validation should check:

- document completeness,
- signature presence,
- clause and attachment consistency,
- value consistency across documents,
- date consistency across transaction milestones,
- release readiness and dependency closure.

### 4.4 Reasoning and simplification

The backend should translate governed extraction and validation results into:

- simple summaries for the frontend,
- role-specific explanations,
- anomaly narratives,
- compliance-linked status messages,
- recommended remediation actions.

## 5. Anomaly detection model

The system should explicitly detect anomalies such as:

- missing attachments or schedules,
- inconsistent names, dates, addresses, or transaction values,
- title records that conflict with contract assumptions,
- insurance coverage values that do not match lender or asset expectations,
- immigration evidence dependencies that are still unresolved,
- suspicious cross-border source-of-funds or beneficial-owner gaps.

Each anomaly should preserve:

- severity,
- affected documents,
- explanation,
- recommended action,
- audit references.

## 6. Compliance and governance

This capability should remain aligned to:

- **ISO/IEC 42001** for accountable AI reasoning and controlled release,
- **ISO/IEC 5259** for data-quality and evaluation discipline,
- **ISO/IEC 27001** for access, evidence, and security controls,
- **ISO/IEC 27701** for purpose-bound document privacy,
- **KYC / AML / sanctions / source-of-funds** requirements for cross-border and investor-led flows,
- **SOC 2 Type 2** expectations for logging, traceability, and controlled operations.

## 7. Auditability requirements

Every document intelligence action should record:

- who or what processed the file,
- what parser or model version was used,
- which fields were extracted,
- which validations passed or failed,
- which anomalies were raised,
- what simplified summary was released to the frontend,
- which user or role viewed or exported the result.

Audit records should be replayable so legal and compliance teams can reconstruct how a summary or anomaly was produced.

## 8. Frontend contract

The frontend-facing packet should expose:

- portfolio or workspace name,
- simplified summary,
- reasoning summary,
- frontend-safe insights,
- governed document metadata,
- extracted fields,
- validation checks,
- anomaly signals,
- compliance findings,
- audit records,
- release status,
- recommended actions.

This lets the UI remain elegant and understandable without bypassing backend policy enforcement.

## 9. Repository mapping

This design is currently represented in:

- `backend/orchestration.py` for the reference packet model and decision assembly,
- `backend/api_contract.json` for the packet schema and endpoint contract,
- `frontend/` for the simplified insight surface,
- `scripts/export_demo_payloads.py` for the generated demo snapshot,
- `scripts/check_frontend_wiring.py` for snapshot-contract verification.
