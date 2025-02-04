# Number-to-words-conversion-using-vector.dev

### **Procedure to Run the Number-to-Words Conversion Pipeline using Vector & Flask**  

This guide will help you set up and run the pipeline step by step.  

---

## **Step 1: Install Dependencies**  
Ensure you have the necessary dependencies installed.  

```bash
pip install flask num2words
```

Download and install **Vector** from [Vector's official site](https://vector.dev/download/).  

---

## **Step 2: Create Required Files**  

### **1. Create the API (`api.py`)**  

### **2. Create the Configuration File (`config.json`)**  

### **3. Create the Vector Pipeline (`vector.yaml`)**  

---
## **Step 3: Run the Flask API**  
Start the API server in a terminal:  

```bash
python api.py
```

It should start on `http://127.0.0.1:5000`.

---

## **Step 4: Run the Vector Pipeline**  
In a separate terminal, run the Vector pipeline:  

```bash
vector --config vector.yaml
```

---

## **Step 5: Verify the Output**  
Check if `output.json` is created with the expected data:  

```json
{
    "number": 26,
    "words": "twenty-six"
}
```

---

## **Step 6: Debugging & Error Handling**  

- **If `config.json` is missing or invalid** → The API will return an error.  
- **If the API is not running** → Vector will retry 3 times before failing.  
- **If `output.json` is empty** → Ensure the API is returning the correct response by testing:  

  ```bash
  curl http://127.0.0.1:5000/data
  ```

---

### **Expected Outcome**  
This procedure sets up a pipeline that:  
- Reads a number from `config.json`.  
- Converts it into words using the Flask API.  
- Writes the result to `output.json` using Vector.  
