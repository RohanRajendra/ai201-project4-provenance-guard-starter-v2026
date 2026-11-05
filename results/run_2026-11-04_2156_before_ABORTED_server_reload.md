# Run log — before

- Produced by: `run_eval.py::main`
- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`
- 3 trials per criterion · 2026-11-04 21:56

Fill in Target from `criteria.md`, and Run and Verdict from the output
underneath. Whether a trial passed depends on the criterion you wrote.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. my own writing |  |   |   |   |  |
| 2. spread ai |  |   |   |   |  |
| 2. spread human |  |   |   |   |  |
| 3. coverage |  |   |   |   |  |
| 5. bad input |  |   |   |   |  |
| 5. boundary 10000 |  |   |   |   |  |

---

## What actually came back

Real output. Paste the relevant parts into your README — the rubric
asks for the actual JSON, not a description of it.

### my own writing

**Trial 1**

```json
[
  {
    "status": null,
    "error": "ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))",
    "sent": "The GuiController represents the class that acts as a controller in th"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.356,
    "model_score": 0.4585,
    "style_score": 0.5071,
    "label": "This piece looks like it was written by a person.",
    "sent": "The top priority is to get started on the job hunt in a serious manner"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3803,
    "model_score": 0.4628,
    "style_score": 0.5958,
    "label": "This piece looks like it was written by a person.",
    "sent": "A 'one world government' would make the human race collectively more e"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.479,
    "model_score": 0.4504,
    "style_score": 0.719,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "In the light of innovation and technology, computers captivate as they"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.405,
    "model_score": 0.531,
    "style_score": 0.5579,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "As an active member of the basketball team on campus, this student, fi"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6332,
    "model_score": 0.6226,
    "style_score": 0.7635,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Additionally, I had the opportunity to collaborate with the student as"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3284,
    "model_score": 0.3976,
    "style_score": 0.5184,
    "label": "This piece looks like it was written by a person.",
    "sent": "Let me tell you a little something about the humble grape. It is often"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5958,
    "model_score": 0.7543,
    "style_score": 0.8746,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "I woke up later than I wanted to today. This pushed all my meals up by"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.538,
    "model_score": 0.7083,
    "style_score": 0.7355,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Using the resale marketplace is a rollercoaster of an experience. For "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4926,
    "model_score": 0.5552,
    "style_score": 0.8598,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "I went to university today. Stopped by the student centre to grab coff"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3277,
    "model_score": 0.4958,
    "style_score": 0.3191,
    "label": "This piece looks like it was written by a person.",
    "sent": "The GuiController represents the class that acts as a controller in th"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.356,
    "model_score": 0.4585,
    "style_score": 0.5071,
    "label": "This piece looks like it was written by a person.",
    "sent": "The top priority is to get started on the job hunt in a serious manner"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3803,
    "model_score": 0.4628,
    "style_score": 0.5958,
    "label": "This piece looks like it was written by a person.",
    "sent": "A 'one world government' would make the human race collectively more e"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.479,
    "model_score": 0.4504,
    "style_score": 0.719,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "In the light of innovation and technology, computers captivate as they"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.405,
    "model_score": 0.531,
    "style_score": 0.5579,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "As an active member of the basketball team on campus, this student, fi"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6332,
    "model_score": 0.6226,
    "style_score": 0.7635,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Additionally, I had the opportunity to collaborate with the student as"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3284,
    "model_score": 0.3976,
    "style_score": 0.5184,
    "label": "This piece looks like it was written by a person.",
    "sent": "Let me tell you a little something about the humble grape. It is often"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5958,
    "model_score": 0.7543,
    "style_score": 0.8746,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "I woke up later than I wanted to today. This pushed all my meals up by"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.538,
    "model_score": 0.7083,
    "style_score": 0.7355,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Using the resale marketplace is a rollercoaster of an experience. For "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4926,
    "model_score": 0.5552,
    "style_score": 0.8598,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "I went to university today. Stopped by the student centre to grab coff"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3277,
    "model_score": 0.4958,
    "style_score": 0.3191,
    "label": "This piece looks like it was written by a person.",
    "sent": "The GuiController represents the class that acts as a controller in th"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.356,
    "model_score": 0.4585,
    "style_score": 0.5071,
    "label": "This piece looks like it was written by a person.",
    "sent": "The top priority is to get started on the job hunt in a serious manner"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3803,
    "model_score": 0.4628,
    "style_score": 0.5958,
    "label": "This piece looks like it was written by a person.",
    "sent": "A 'one world government' would make the human race collectively more e"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.479,
    "model_score": 0.4504,
    "style_score": 0.719,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "In the light of innovation and technology, computers captivate as they"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.405,
    "model_score": 0.531,
    "style_score": 0.5579,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "As an active member of the basketball team on campus, this student, fi"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6332,
    "model_score": 0.6226,
    "style_score": 0.7635,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Additionally, I had the opportunity to collaborate with the student as"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3284,
    "model_score": 0.3976,
    "style_score": 0.5184,
    "label": "This piece looks like it was written by a person.",
    "sent": "Let me tell you a little something about the humble grape. It is often"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5958,
    "model_score": 0.7543,
    "style_score": 0.8746,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "I woke up later than I wanted to today. This pushed all my meals up by"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.538,
    "model_score": 0.7083,
    "style_score": 0.7355,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Using the resale marketplace is a rollercoaster of an experience. For "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4926,
    "model_score": 0.5552,
    "style_score": 0.8598,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "I went to university today. Stopped by the student centre to grab coff"
  }
]
```

### spread ai

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5242,
    "model_score": 0.6635,
    "style_score": 0.563,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Photosynthesis is the process by which plants, algae, and some bacteri"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.568,
    "model_score": 0.7551,
    "style_score": 0.7618,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Inflation is the sustained rise in the general level of prices across "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4434,
    "model_score": 0.5709,
    "style_score": 0.6318,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Plate tectonics is the scientific theory explaining how Earth's outer "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.518,
    "model_score": 0.614,
    "style_score": 0.8439,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Vaccines work by training the immune system to recognize a pathogen be"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6134,
    "model_score": 0.7948,
    "style_score": 0.8641,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Water moves continuously between the oceans, the atmosphere, and the l"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5242,
    "model_score": 0.6635,
    "style_score": 0.563,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Photosynthesis is the process by which plants, algae, and some bacteri"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.568,
    "model_score": 0.7551,
    "style_score": 0.7618,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Inflation is the sustained rise in the general level of prices across "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4434,
    "model_score": 0.5709,
    "style_score": 0.6318,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Plate tectonics is the scientific theory explaining how Earth's outer "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.518,
    "model_score": 0.614,
    "style_score": 0.8439,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Vaccines work by training the immune system to recognize a pathogen be"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6134,
    "model_score": 0.7948,
    "style_score": 0.8641,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Water moves continuously between the oceans, the atmosphere, and the l"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5242,
    "model_score": 0.6635,
    "style_score": 0.563,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Photosynthesis is the process by which plants, algae, and some bacteri"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.568,
    "model_score": 0.7551,
    "style_score": 0.7618,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Inflation is the sustained rise in the general level of prices across "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4434,
    "model_score": 0.5709,
    "style_score": 0.6318,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Plate tectonics is the scientific theory explaining how Earth's outer "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.518,
    "model_score": 0.614,
    "style_score": 0.8439,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Vaccines work by training the immune system to recognize a pathogen be"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6134,
    "model_score": 0.7948,
    "style_score": 0.8641,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Water moves continuously between the oceans, the atmosphere, and the l"
  }
]
```

### spread human

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4312,
    "model_score": 0.4679,
    "style_score": 0.6375,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "It is interesting to contemplate an entangled bank, clothed with many "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4772,
    "model_score": 0.5986,
    "style_score": 0.5558,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "I went to the woods because I wished to live deliberately, to front on"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4398,
    "model_score": 0.6528,
    "style_score": 0.4537,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "The plan which I adopted, and the one by which I was most successful, "
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.28,
    "model_score": 0.4619,
    "style_score": 0.1961,
    "label": "This piece looks like it was written by a person.",
    "sent": "Now when I had mastered the language of this water and had come to kno"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2554,
    "model_score": 0.4682,
    "style_score": 0.0852,
    "label": "This piece looks like it was written by a person.",
    "sent": "It was on a dreary night of November that I beheld the accomplishment "
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4312,
    "model_score": 0.4679,
    "style_score": 0.6375,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "It is interesting to contemplate an entangled bank, clothed with many "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4772,
    "model_score": 0.5986,
    "style_score": 0.5558,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "I went to the woods because I wished to live deliberately, to front on"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4398,
    "model_score": 0.6528,
    "style_score": 0.4537,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "The plan which I adopted, and the one by which I was most successful, "
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.28,
    "model_score": 0.4619,
    "style_score": 0.1961,
    "label": "This piece looks like it was written by a person.",
    "sent": "Now when I had mastered the language of this water and had come to kno"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2554,
    "model_score": 0.4682,
    "style_score": 0.0852,
    "label": "This piece looks like it was written by a person.",
    "sent": "It was on a dreary night of November that I beheld the accomplishment "
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4312,
    "model_score": 0.4679,
    "style_score": 0.6375,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "It is interesting to contemplate an entangled bank, clothed with many "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4772,
    "model_score": 0.5986,
    "style_score": 0.5558,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "I went to the woods because I wished to live deliberately, to front on"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4398,
    "model_score": 0.6528,
    "style_score": 0.4537,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "The plan which I adopted, and the one by which I was most successful, "
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.28,
    "model_score": 0.4619,
    "style_score": 0.1961,
    "label": "This piece looks like it was written by a person.",
    "sent": "Now when I had mastered the language of this water and had come to kno"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2554,
    "model_score": 0.4682,
    "style_score": 0.0852,
    "label": "This piece looks like it was written by a person.",
    "sent": "It was on a dreary night of November that I beheld the accomplishment "
  }
]
```

### coverage

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.8369,
    "model_score": 0.7738,
    "style_score": 0.8,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "The impact of social media on teenagers is a subject of considerable d"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.7972,
    "model_score": 0.6944,
    "style_score": 0.7999,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Remote work has transformed the modern workplace, offering both signif"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8592,
    "model_score": 0.8184,
    "style_score": 0.8,
    "label": "Our check found strong signs that this piece may have been written by an AI tool, but this is not proof and the check can be wrong. Nothing has been taken down. If you wrote this, you can ask for a person to review it and tell them how you wrote it.",
    "sent": "Sleep is essential to physical and mental health, yet it is frequently"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4662,
    "model_score": 0.6956,
    "style_score": 0.4734,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "The parser. The JsonParser interface defines the parsing behaviour for"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.38,
    "model_score": 0.581,
    "style_score": 0.3581,
    "label": "This piece looks like it was written by a person.",
    "sent": "Had enough of lazing around, getting nothing done. Just wrapped up the"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3845,
    "model_score": 0.5484,
    "style_score": 0.441,
    "label": "This piece looks like it was written by a person.",
    "sent": "Fighting is ultimate, ppl love ufc because it is not faked or scripted"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4149,
    "model_score": 0.6085,
    "style_score": 0.4425,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Let me tell you a little something about the humble grape. It is often"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4023,
    "model_score": 0.4845,
    "style_score": 0.6404,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "A 'one world government' would make the human race collectively more e"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3372,
    "model_score": 0.4422,
    "style_score": 0.4644,
    "label": "This piece looks like it was written by a person.",
    "sent": "The top priority is to get started on the job hunt in a serious manner"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.8369,
    "model_score": 0.7738,
    "style_score": 0.8,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "The impact of social media on teenagers is a subject of considerable d"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.7972,
    "model_score": 0.6944,
    "style_score": 0.7999,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Remote work has transformed the modern workplace, offering both signif"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8592,
    "model_score": 0.8184,
    "style_score": 0.8,
    "label": "Our check found strong signs that this piece may have been written by an AI tool, but this is not proof and the check can be wrong. Nothing has been taken down. If you wrote this, you can ask for a person to review it and tell them how you wrote it.",
    "sent": "Sleep is essential to physical and mental health, yet it is frequently"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4662,
    "model_score": 0.6956,
    "style_score": 0.4734,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "The parser. The JsonParser interface defines the parsing behaviour for"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.38,
    "model_score": 0.581,
    "style_score": 0.3581,
    "label": "This piece looks like it was written by a person.",
    "sent": "Had enough of lazing around, getting nothing done. Just wrapped up the"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3845,
    "model_score": 0.5484,
    "style_score": 0.441,
    "label": "This piece looks like it was written by a person.",
    "sent": "Fighting is ultimate, ppl love ufc because it is not faked or scripted"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4149,
    "model_score": 0.6085,
    "style_score": 0.4425,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Let me tell you a little something about the humble grape. It is often"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4023,
    "model_score": 0.4845,
    "style_score": 0.6404,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "A 'one world government' would make the human race collectively more e"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3372,
    "model_score": 0.4422,
    "style_score": 0.4644,
    "label": "This piece looks like it was written by a person.",
    "sent": "The top priority is to get started on the job hunt in a serious manner"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.8369,
    "model_score": 0.7738,
    "style_score": 0.8,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "The impact of social media on teenagers is a subject of considerable d"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.7972,
    "model_score": 0.6944,
    "style_score": 0.7999,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Remote work has transformed the modern workplace, offering both signif"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8592,
    "model_score": 0.8184,
    "style_score": 0.8,
    "label": "Our check found strong signs that this piece may have been written by an AI tool, but this is not proof and the check can be wrong. Nothing has been taken down. If you wrote this, you can ask for a person to review it and tell them how you wrote it.",
    "sent": "Sleep is essential to physical and mental health, yet it is frequently"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4662,
    "model_score": 0.6956,
    "style_score": 0.4734,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "The parser. The JsonParser interface defines the parsing behaviour for"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.38,
    "model_score": 0.581,
    "style_score": 0.3581,
    "label": "This piece looks like it was written by a person.",
    "sent": "Had enough of lazing around, getting nothing done. Just wrapped up the"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3845,
    "model_score": 0.5484,
    "style_score": 0.441,
    "label": "This piece looks like it was written by a person.",
    "sent": "Fighting is ultimate, ppl love ufc because it is not faked or scripted"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4149,
    "model_score": 0.6085,
    "style_score": 0.4425,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "Let me tell you a little something about the humble grape. It is often"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4023,
    "model_score": 0.4845,
    "style_score": 0.6404,
    "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
    "sent": "A 'one world government' would make the human race collectively more e"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3372,
    "model_score": 0.4422,
    "style_score": 0.4644,
    "label": "This piece looks like it was written by a person.",
    "sent": "The top priority is to get started on the job hunt in a serious manner"
  }
]
```

### bad input

**Trial 1**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_1\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": " \n\t"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_4\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": 123, \"creator_id\": \"eval_bad_5\"}"
  },
  {
    "status": 413,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  },
  {
    "status": 413,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "word word word word word word word word word word word word word word "
  },
  {
    "status": 422,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "Hi"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_1\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": " \n\t"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_4\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": 123, \"creator_id\": \"eval_bad_5\"}"
  },
  {
    "status": 413,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  },
  {
    "status": 413,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "word word word word word word word word word word word word word word "
  },
  {
    "status": 422,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "Hi"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_1\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": " \n\t"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_4\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": 123, \"creator_id\": \"eval_bad_5\"}"
  },
  {
    "status": 413,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  },
  {
    "status": 413,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "word word word word word word word word word word word word word word "
  },
  {
    "status": 422,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "Hi"
  }
]
```

### boundary 10000

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3612,
    "model_score": 0.5214,
    "style_score": 0.3301,
    "label": "This piece looks like it was written by a person.",
    "sent": "It is interesting to contemplate an entangled bank, clothed with many "
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3612,
    "model_score": 0.5214,
    "style_score": 0.3301,
    "label": "This piece looks like it was written by a person.",
    "sent": "It is interesting to contemplate an entangled bank, clothed with many "
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3612,
    "model_score": 0.5214,
    "style_score": 0.3301,
    "label": "This piece looks like it was written by a person.",
    "sent": "It is interesting to contemplate an entangled bank, clothed with many "
  }
]
```
