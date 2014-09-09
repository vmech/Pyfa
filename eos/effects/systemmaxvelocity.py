# Used by:
# Celestials named like: Black Hole Effect Beacon Class (6 of 6)
runTime = "early"
type = ("projected", "offline")
def handler(fit, beacon, context):
    fit.ship.multiplyItemAttr("maxVelocity", beacon.getModifiedItemAttr("maxVelocityMultiplier"), stackingPenalties=True, penaltyGroup="postMul")
