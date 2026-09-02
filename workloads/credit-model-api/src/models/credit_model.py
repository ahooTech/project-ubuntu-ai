# credit_model.py
import logging

logger = logging.getLogger(__name__)

class CreditScoringModel:
    """
    A mock credit scoring model. 
    In production, this would load a trained model from Databricks/MLflow.
    """
    
    def __init__(self, version: str):
        self.version = version
        logger.info(f"Initialized mock credit scoring model version: {self.version}")

    def predict(self, annual_income: float, monthly_debt: float, credit_history_years: int) -> dict:
        """
        Calculates a mock credit score and decision.
        """
        # Simple mock logic: Higher income and history = better score. Higher debt = worse.
        debt_to_income_ratio = monthly_debt / (annual_income / 12) if annual_income > 0 else 1.0
        
        base_score = 300
        score = base_score + (credit_history_years * 15) - (debt_to_income_ratio * 100)
        
        # Clamp score between 300 and 850
        final_score = max(300, min(850, int(score)))
        
        decision = "Approved" if final_score >= 650 else "Declined"
        
        logger.info(f"Prediction made: Score={final_score}, Decision={decision}, DTI={debt_to_income_ratio:.2f}")
        
        return {
            "credit_score": final_score,
            "decision": decision,
            "model_version": self.version,
            "risk_factors": {
                "debt_to_income_ratio": round(debt_to_income_ratio, 2)
            }
        }

# Singleton instance for the application
_model_instance = None

def get_model(version: str) -> CreditScoringModel:
    global _model_instance
    if _model_instance is None:
        _model_instance = CreditScoringModel(version=version)
    return _model_instance