# Predictive Market Intelligence Engine

## Purpose

The Predictive Market Intelligence Engine gives EstateOS a macro-to-micro forecasting layer that continuously analyzes:

- global and local real-estate trend signals,
- interest rates and mortgage conditions,
- migration and mobility flows,
- supply-demand imbalance,
- investor liquidity and affordability pressure, and
- scenario-driven forward-looking market alerts.

Its goal is to let the frontend surface explainable market outlooks while the backend continuously ingests data, retrains models, and publishes governed signals for investors, brokers, and analysts.

## Functional design

### Frontend outcomes

The frontend should be able to show:

- market scope and investment horizon,
- signal summaries for the active geography,
- horizon forecasts for price growth, rent growth, and cap-rate movement,
- severity-based alerts when rates, migration, or supply change the investment case,
- pipeline health indicators so analysts know whether signals are fresh.

### Backend responsibilities

The backend engine should:

1. ingest streaming macro, migration, and local-market data,
2. normalize those feeds into a governed feature store,
3. retrain horizon-specific forecasting models on a scheduled cadence,
4. publish explainable forward-looking signals and alerts,
5. preserve model-governance, data-quality, and audit evidence.

## Data streams

The current reference design uses three canonical stream families:

- **Global macro and rate feed** for policy rates, inflation, FX, mortgage spreads, and financing sensitivity.
- **Migration and mobility ledger** for cross-border investor movement, household relocation demand, visa interest, and origin-destination flows.
- **Supply-demand monitor** for inventory, absorption, new supply, days on market, rent velocity, and concession behavior.

## Forecasting outputs

The engine emits:

- **Indicators** describing the current market state.
- **Forecast scenarios** across multiple horizons.
- **Alerts** that tell the frontend which changing conditions matter now.
- **Pipeline-status signals** showing ingest, feature refresh, retraining, and publication health.

## Governance posture

The market engine is intended to remain aligned with:

- **ISO/IEC 42001** for AI management,
- **ISO/IEC 5259** for data quality,
- **ISO/IEC 27001** for access, logging, and platform protection,
- **ISO 31000** for risk framing.

## Repository mapping

The current reference implementation lands in:

- `backend/orchestration.py` for the packet model and demo signal generation,
- `backend/api_contract.json` for the API schema contract,
- `frontend/` for the visual workspace and alerts surface,
- `scripts/export_demo_payloads.py` for the stable demo snapshot consumed by the prototype.
