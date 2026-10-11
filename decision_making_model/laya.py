from laya import Router
import warnings
## Suppress specific Laya runtime warnings
warnings.filterwarnings("ignore", category=RuntimeWarning, module="laya")


router = Router(preload=True)  # downloads a checkpoint on first use; Router(preload=True) loads all three up front

state = "Hi, can you send me the quotation"
questions = {
    "department": {"type": "choice", "instructions": "Which department should handle this?",
                   "criteria": {"billing": "invoices, payments, refunds",
                                "technical": "bugs, outages, system errors",
                                "sales": "i am interested in buying product,",
                                "other": "everything else"}},

    "urgency": {"type": "score", "instructions": "How urgent is this?",
                "criteria": ["not urgent", "soon", "blocking"]},

    "churn_risk": {"type": "noul", "instructions": "Does the user threaten to cancel or leave?"},
}

result = router.predict(state, questions)

print(result)
print(result["answers"]["department"]["choice"])  # billing
print(result["answers"]["churn_risk"]["noul"])    # probability the answer is yes
print(result["routing"]["model"])                 # english