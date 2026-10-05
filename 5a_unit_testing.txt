from EmotionDetection import emotion_detector

def run_tests():
    test_cases = [
        ("I am glad this happened", "joy"),
        ("I am really mad about this", "anger"),
        ("I feel disgusted just hearing about this", "disgust"),
        ("I am so sad about this", "sadness"),
        ("I am really afraid that this will happen", "fear")
    ]

    for statement, expected_emotion in test_cases:
        result = emotion_detector(statement)
        actual_emotion = result['dominant_emotion']
        
        if actual_emotion == expected_emotion:
            print(f"PASSED: '{statement}' -> {actual_emotion}")
        else:
            print(f"FAILED: '{statement}' -> Expected {expected_emotion}, but got {actual_emotion}")

if __name__ == "__main__":
    run_tests()
