stress_ratio = 0.5
strength = 92.3
toughness = 0.788

delta_f = 2.0 * toughness / strength

parameters = {
	"results": [
		{
            "type": "max",
			"step": "Load",
            "identifier":
                {
                    "symbol": "S13",
                    "elset": "COHESIVE",
                    "position": "Element 1 Int Point 1"
                },
            "referenceValue": strength * stress_ratio,
            "tolerance": strength * 0.001
        },
		{
            "type": "max",
			"step": "Fatigue",
            "identifier":
                {
                    "symbol": "S13",
                    "elset": "COHESIVE",
                    "position": "Element 1 Int Point 1"
                },
            "referenceValue": strength * stress_ratio,
            "tolerance": strength * 0.003
        },
        {
            "type": "disp_at_zero_y",
            "step": "Fatigue",
            "identifier": [
                { # x
                    "symbol": "U1",
                    "nset": "Z+",
                    "position": "Node 5"
                },
                { # y
                    "symbol": "S13",
                    "elset": "COHESIVE",
                    "position": "Element 1 Int Point 1"
                }
            ],
            "window": [delta_f * 0.80, delta_f * 1.20],
            "zeroTol": strength * 0.001,  # Defines how close to zero the y value needs to be
            "referenceValue": delta_f,
            "tolerance": delta_f * 0.05
        },
        {
            "type": "max",
			"step": "Fatigue",
            "identifier":
                {
                    "symbol": "SDV_COH_dmg",
                    "elset": "COHESIVE",
                    "position": "Element 1 Int Point 1"
                },
            "referenceValue": 1.0,
            "tolerance": 0.0
        },
        {
            "type": "continuous",
			"step": "Fatigue",
            "identifier":
                {
                    "symbol": "S13",
                    "elset": "COHESIVE",
                    "position": "Element 1 Int Point 1"
                },
            "referenceValue": 0.0,
            "tolerance": strength * 0.1
        }
	]
}
