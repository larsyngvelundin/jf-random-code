question_texts = [
    "How often do you find yourself being overly critical of yourself?",
    "How often do you judge others for their mistakes or shortcomings?",
    "How often do you criticize circumstances or complain about your life?",
    "How frequently do you feel the need to control or micromanage others?",
    "How often do you get anxious when things don’t go according to your plan?",
    "How frequently do you feel stressed about deadlines or deliverables?",
    "How often do you strive for perfection and get upset when things aren’t perfect?",
    "How frequently do you set extremely high standards for yourself and others?",
    "How often do you feel irritated when others don’t meet your expectations?",
    "How often do you feel compelled to please others, even at your own expense?",
    "How frequently do you avoid conflict to keep others happy?",
    "How often do you seek approval from others to feel valued?",
    "How often do you find it difficult to stay focused on one task without getting bored?",
    "How frequently do you jump from one activity to another without completing them?",
    "How often do you feel uneasy or restless when things are too calm?",
    "How often do you tie your self-worth to your accomplishments?",
    "How frequently do you feel that you must be the best at everything you do?",
    "How often do you push yourself beyond your limits to achieve more?",
    "How often do you feel like life is unfair and that you are treated unjustly?",
    "How frequently do you dwell on your problems and feel sorry for yourself?",
    "How often do you seek sympathy or attention for your difficulties?",
    "How often do you prioritize logic and reason over feelings and emotions?",
    "How frequently do you find it difficult to empathize with others?",
    "How often do you dismiss emotions as irrelevant in decision-making?",
    "How often do you feel constantly on edge, anticipating problems?",
    "How frequently do you worry about what could go wrong in any situation?",
    "How often do you feel the need to stay alert and cautious at all times?",
    "How often do you avoid difficult conversations or unpleasant tasks?",
    "How frequently do you procrastinate on tasks that you don’t enjoy?",
    "How often do you focus on the positive and ignore the negative aspects of situations?",
]

for i in range(0, len(question_texts)):
    # questions[1][type]:control_radio
    print(f"questions[{i + 1}][type]:control_radio")

    # questions[1][calcValues]:0|1|2|3|4
    print(f"questions[{i + 1}][calcValues]:0|1|2|3|4")

    # questions[1][order]:2
    print(f"questions[{i + 1}][order]:{i + 2}")

    # questions[1][options]:Never|Rarely|Sometimes|Often|Always
    print(f"questions[{i + 1}][options]:Never|Rarely|Sometimes|Often|Always")

    # questions[1][text]:How often do you find yourself being overly critical of yourself?
    print(f"questions[{i + 1}][text]:{question_texts[i]}")

    # questions[1][spreadCols]:5
    print(f"questions[{i + 1}][spreadCols]:5")
