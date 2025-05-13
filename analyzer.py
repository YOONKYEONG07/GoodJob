# analyzer.py

def analyze_resume(text):
    result = {
        "word_count": len(text.split()),
        "char_count": len(text),
        "tip": "분량이 적절해요!" if 300 <= len(text) <= 1000 else "자기소개서 분량을 조절해 보세요."
    }
    return result
