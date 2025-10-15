# 👁️ Face Detection App — Powered by OpenCV

**Author:** [Yogesh Madhukar Borse](https://github.com/Yogesh-borse)  
**License:** Apache-2.0  
**Tech Stack:** Python, OpenCV, Matplotlib (optional)

---

## 📌 Overview

This project demonstrates **real-time face detection** using Python and OpenCV.  
It compares two powerful classifiers — **Haar Cascade** and **LBP Cascade** — and benchmarks their performance in terms of **accuracy** and **speed**.

The goal is to detect human faces in images or video streams efficiently while learning the inner working of OpenCV’s machine learning models.

---

## 🧠 Algorithms Explained

### 🔹 Haar Cascade Classifier
A machine-learning-based approach using thousands of positive (face) and negative (non-face) images.

**Pipeline:**
1. **Haar Feature Selection** — Identifies rectangular regions to extract intensity differences.  
2. **Integral Image** — Reduces computation by using summed area tables.  
3. **AdaBoost** — Selects the most relevant features.  
4. **Cascading Classifiers** — Applies multiple stages to filter non-face regions.

**Pros:**  
✅ High detection accuracy  
✅ Low false positives  

**Cons:**  
⚠️ Computationally heavy  
⚠️ Less robust to lighting or occlusion  

---

### 🔹 LBP (Local Binary Pattern) Cascade Classifier
LBP describes local textures using binary patterns and is faster than Haar.

**Pipeline:**
1. **LBP Labeling** — Assigns binary labels to pixels.  
2. **Feature Vector Construction** — Builds histograms of texture patterns.  
3. **Gentle AdaBoost** — Removes redundant features.  
4. **Cascade of Classifiers** — Filters image regions progressively.

**Pros:**  
✅ Fast and simple  
✅ Works well under illumination changes  

**Cons:**  
⚠️ Slightly less accurate  
⚠️ More false positives  

---

## ⚖️ Haar vs LBP — Comparison

| Classifier | Pros | Cons |
|-------------|------|------|
| **Haar** | High accuracy, fewer false positives | Slower, not robust to occlusion |
| **LBP** | Fast, lightweight, good under poor lighting | Slightly lower accuracy, more false positives |

---

## 🧪 Benchmarking Summary

### 🖼️ Test 1 — `test5.jpg`
- ✅ Both classifiers detected all faces correctly  
- ⚡ LBP executed faster  

### 🖼️ Test 2 — `test6.jpg`
- 🎯 Haar detected more faces accurately  
- ⚡ LBP was much faster  

**Result:**  
> Haar = Better Accuracy  
> LBP = Better Speed  

---

## 🛠️ Dependencies

Make sure the following are installed before running the app:

```bash
pip install opencv-python matplotlib numpy
