import React, { useState } from 'react';

const GRADE_OPTIONS = ["Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8"];
const TYPE_OPTIONS = ["Question Paper", "Worksheet"]
const DIFFICULTY_OPTIONS = ["Easy", "Medium", "Difficult"];

export default function IndexPage() {
     const [form, SetForm] = useState({
          grade: "Grade 1",
          chapter: "",
          type: "Question Paper",
          difficulty: "Easy",
     })
     const [result, setResult] = useState(null);
     const [loading, setLoading] = useState(false);

     const handleChange = (e) => {
          setForm({ ...form, [e.target.name]: e.target.value });
     };

     const handleSubmit = async (e) => {
          e.preventDefault();
          setLoading(true);
          setResult(null);
          const res = await fetch("/api/generate", {
               method: "POST",
               headers: { "Content-Type": "application/json" },
               body: JSON.stringify(form)
          });
          const data = await res.json();
          setResult(data);
          setLoading(false);
     };

return (
     <div style = {{maxWidth: 600, margin: "auto", padding: 20}}>
          <h2>AI Material Generator</h2>
          <form onSubmit={handleSubmit}>
               <label>
                    Grade:
                    <select name = "grade" value = {form.grade} onChange = {handleChange}>
                         {GRADE_OPTIONS.map(g => <option key = {g}>{g}</option>)}
                    </select>
               </label>
               <br/>
               <label>
                    Chapter/Unit:
                    <input name = "chapter" value = {form.chapter} onChange = {handleChange} required style = {{width: "100%"}} />
               </label>
               <br/>
               <label>
                    Material Type:
                    <select name = "type" value = {form.type} onChange = {handleChange}>
                         {TYPE_OPTIONS.map(t => <option key = {t}>{t}</option>)}
                    </select>
               </label>
               <br/>
               <button type = "submit" disabled = {loading}>{loading ? "Generating..." : "Generate"}</button>
          </form>
          {result && (
               <div style = {{marginTop: 30}}>
                    <h3>Generated Output</h3>
                    <pre style = {{background: "#f6f6f6", padding: 10, borderRadius: 6}}>{result.paper}</pre>
                    <a href = {result.pdf_url} download target = "_blank" rel = "noopener noreferrer">Download PDF</a> |{" "}
                    <a href = {result.docx_url} download target = "_blank" rel = "noopener noreferrer">Download Word Doc</a>
               </div>
          )}
     </div>
);
}