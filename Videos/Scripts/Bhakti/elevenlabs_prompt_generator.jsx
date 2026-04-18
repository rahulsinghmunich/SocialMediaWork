import { useState, useRef, useEffect } from "react";

const SYSTEM_PROMPT = `You are an expert ElevenLabs V3 Audio Tag prompt engineer specializing in Hindi devotional (bhakti) narration for Sanatan Dharma content.

You will receive a script with multiple scenes. Each scene has a NARRATION line in Hindi.

Your job: Convert ALL narrations into ONE single continuous ElevenLabs V3 prompt with proper audio tags.

RULES:
1. Extract ONLY the narration text from each scene
2. Add ElevenLabs V3 audio tags before/between lines to control emotion, delivery, pacing
3. Use ONLY these proven V3 audio tags:
   - Emotions: [sorrowful], [excited], [angry], [calm], [curious], [nervous], [fearless]
   - Delivery: [whispers], [shouts], [shouting], [drawn out], [fast-paced], [rushed], [steady]
   - Reactions: [sighs], [gasps], [laughs], [pause], [short pause], [long pause]
   - Tone: [dramatic], [reverent], [prophetic], [warm], [gentle], [intense], [heroic], [ominous], [dark tone], [proud], [wise], [peaceful], [triumphant], [devotional]
   - Performance: [deep voice], [rising intensity]
4. Use the scene's EMOTION tag to guide which audio tags to apply
5. Add [pause] between scenes and [long pause] between major emotional shifts
6. Use ... (ellipsis) for dramatic pauses within sentences
7. Use CAPITALS for emphasis on key words
8. Keep the Hindi text EXACTLY as written — do NOT translate or modify the narration words
9. Match tags to the scene emotion:
   - भय (fear) → [ominous][dark tone]
   - करुणा (compassion) → [sorrowful][sad]
   - रोमांच (thrill) → [rising intensity][excited]
   - श्रद्धा (devotion) → [reverent][drawn out]
   - वीरता (valor) → [heroic][intense]
   - आनंद (joy) → [warm][peaceful]
10. Output ONLY the final prompt text — no explanations, no markdown, no scene numbers, no labels

EXAMPLE OUTPUT FORMAT:
[deep voice][dramatic] जब सारे देवता हार गए... [pause] [shouting] तब प्रकट हुई वो शक्ति जिसने ब्रह्मांड बदल दिया!

[long pause]

[ominous][dark tone] जब महिषासुर ने देवताओं को पराजित कर दिया... [pause] [sorrowful] तब तीनों लोकों में भय छा गया।

...and so on for all scenes.`;

const DEFAULT_PLACEHOLDER = `🎬 SCENE 1 — [0:00–0:07]
📸 VISUAL PROMPT:
Mahishasura in his massive buffalo-demon form...
🎥 MOTION PROMPT:
Slow dramatic tilt up...
🎙️ NARRATION:
"जब महिषासुर ने देवताओं को पराजित कर दिया… तब तीनों लोकों में भय छा गया।"
💫 EMOTION: भय
🔥 VIRAL SCORE: 8
──────────────────────────────────────
🎬 SCENE 2 — [0:07–0:14]
...paste your full script here...`;

function safeCopy(text) {
  if (navigator.clipboard && navigator.clipboard.writeText) {
    return navigator.clipboard.writeText(text);
  }
  return new Promise((resolve, reject) => {
    const ta = document.createElement("textarea");
    ta.value = text;
    ta.style.position = "fixed";
    ta.style.left = "-9999px";
    document.body.appendChild(ta);
    ta.select();
    try {
      document.execCommand("copy");
      resolve();
    } catch (e) {
      reject(e);
    } finally {
      document.body.removeChild(ta);
    }
  });
}

export default function ElevenLabsGenerator() {
  const [script, setScript] = useState("");
  const [output, setOutput] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [copied, setCopied] = useState(false);
  const [sceneCount, setSceneCount] = useState(0);
  const [streamText, setStreamText] = useState("");
  const outputRef = useRef(null);

  useEffect(() => {
    const matches = script.match(/🎬\s*SCENE/gi);
    setSceneCount(matches ? matches.length : 0);
  }, [script]);

  const handleGenerate = async () => {
    if (!script.trim()) {
      setError("⚠️ Paste your scene script first!");
      return;
    }
    setError("");
    setOutput("");
    setStreamText("");
    setLoading(true);
    setCopied(false);

    try {
      const response = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          model: "claude-sonnet-4-20250514",
          max_tokens: 4000,
          system: SYSTEM_PROMPT,
          messages: [
            {
              role: "user",
              content: `Here is my complete scene script. Convert ALL narrations into ONE continuous ElevenLabs V3 prompt with audio tags:\n\n${script}`,
            },
          ],
        }),
      });

      if (!response.ok) {
        const errData = await response.json().catch(() => ({}));
        throw new Error(errData?.error?.message || `API Error: ${response.status}`);
      }

      const data = await response.json();
      const result = data.content
        .filter((b) => b.type === "text")
        .map((b) => b.text)
        .join("\n");
      setOutput(result);
    } catch (err) {
      setError(`❌ ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  const handleCopy = async () => {
    try {
      await safeCopy(output);
      setCopied(true);
      setTimeout(() => setCopied(false), 2500);
    } catch {
      setError("Copy failed — please select and copy manually");
    }
  };

  const handleClear = () => {
    setScript("");
    setOutput("");
    setError("");
    setCopied(false);
  };

  return (
    <div style={{
      minHeight: "100vh",
      background: "linear-gradient(160deg, #0a0a0f 0%, #1a0a2e 30%, #0f0f1a 70%, #0a0a0f 100%)",
      color: "#e8e0d4",
      fontFamily: "'Segoe UI', system-ui, sans-serif",
      padding: "0",
      overflow: "auto",
    }}>
      {/* Decorative top bar */}
      <div style={{
        height: "4px",
        background: "linear-gradient(90deg, #ff6b00, #ff9500, #ffb700, #ff6b00)",
        width: "100%",
      }} />

      {/* Header */}
      <div style={{
        textAlign: "center",
        padding: "28px 20px 20px",
        borderBottom: "1px solid rgba(255,150,0,0.15)",
      }}>
        <div style={{ fontSize: "14px", letterSpacing: "4px", color: "#ff9500", marginBottom: "8px", textTransform: "uppercase" }}>
          🔱 Sanatan Dharma Production System
        </div>
        <h1 style={{
          fontSize: "28px",
          fontWeight: 800,
          margin: "0 0 6px",
          background: "linear-gradient(135deg, #ff9500, #ffcc00, #ff6b00)",
          WebkitBackgroundClip: "text",
          WebkitTextFillColor: "transparent",
          letterSpacing: "1px",
        }}>
          ElevenLabs V3 Prompt Generator
        </h1>
        <p style={{ fontSize: "13px", color: "#8a8090", margin: 0 }}>
          Paste scene script → Get audio-tagged Hindi narration prompt
        </p>
      </div>

      <div style={{ maxWidth: "900px", margin: "0 auto", padding: "24px 16px" }}>

        {/* Input Section */}
        <div style={{
          background: "rgba(255,255,255,0.03)",
          border: "1px solid rgba(255,150,0,0.12)",
          borderRadius: "12px",
          padding: "20px",
          marginBottom: "20px",
        }}>
          <div style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            marginBottom: "12px",
          }}>
            <label style={{
              fontSize: "14px",
              fontWeight: 700,
              color: "#ff9500",
              letterSpacing: "1px",
              textTransform: "uppercase",
            }}>
              📜 Scene Script Input
            </label>
            {sceneCount > 0 && (
              <span style={{
                fontSize: "12px",
                background: "rgba(255,150,0,0.15)",
                color: "#ffb700",
                padding: "3px 10px",
                borderRadius: "20px",
                fontWeight: 600,
              }}>
                {sceneCount} scene{sceneCount > 1 ? "s" : ""} detected
              </span>
            )}
          </div>

          <textarea
            value={script}
            onChange={(e) => setScript(e.target.value)}
            placeholder={DEFAULT_PLACEHOLDER}
            spellCheck={false}
            style={{
              width: "100%",
              minHeight: "280px",
              background: "rgba(0,0,0,0.4)",
              border: "1px solid rgba(255,150,0,0.2)",
              borderRadius: "8px",
              color: "#e8e0d4",
              fontSize: "13px",
              lineHeight: "1.7",
              padding: "16px",
              resize: "vertical",
              outline: "none",
              fontFamily: "monospace",
              boxSizing: "border-box",
            }}
          />

          {/* Buttons */}
          <div style={{ display: "flex", gap: "12px", marginTop: "16px" }}>
            <button
              onClick={handleGenerate}
              disabled={loading}
              style={{
                flex: 1,
                padding: "14px 24px",
                fontSize: "15px",
                fontWeight: 700,
                color: "#0a0a0f",
                background: loading
                  ? "rgba(255,150,0,0.3)"
                  : "linear-gradient(135deg, #ff9500, #ffb700)",
                border: "none",
                borderRadius: "8px",
                cursor: loading ? "wait" : "pointer",
                letterSpacing: "1px",
                transition: "all 0.2s",
                opacity: loading ? 0.7 : 1,
              }}
            >
              {loading ? (
                <span>
                  <span style={{
                    display: "inline-block",
                    animation: "spin 1s linear infinite",
                    marginRight: "8px",
                  }}>⏳</span>
                  Generating V3 Prompt...
                </span>
              ) : (
                "🎙️ Generate ElevenLabs V3 Prompt"
              )}
            </button>

            <button
              onClick={handleClear}
              style={{
                padding: "14px 20px",
                fontSize: "13px",
                fontWeight: 600,
                color: "#8a8090",
                background: "rgba(255,255,255,0.05)",
                border: "1px solid rgba(255,255,255,0.1)",
                borderRadius: "8px",
                cursor: "pointer",
                transition: "all 0.2s",
              }}
            >
              🗑️ Clear
            </button>
          </div>
        </div>

        {/* Error */}
        {error && (
          <div style={{
            background: "rgba(255,60,60,0.1)",
            border: "1px solid rgba(255,60,60,0.3)",
            borderRadius: "8px",
            padding: "12px 16px",
            marginBottom: "20px",
            fontSize: "13px",
            color: "#ff6b6b",
          }}>
            {error}
          </div>
        )}

        {/* Output Section */}
        {output && (
          <div style={{
            background: "rgba(255,255,255,0.03)",
            border: "1px solid rgba(0,200,100,0.2)",
            borderRadius: "12px",
            padding: "20px",
            marginBottom: "20px",
          }}>
            <div style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              marginBottom: "14px",
            }}>
              <label style={{
                fontSize: "14px",
                fontWeight: 700,
                color: "#00c864",
                letterSpacing: "1px",
                textTransform: "uppercase",
              }}>
                🎙️ ElevenLabs V3 Prompt — Ready to Copy
              </label>
              <button
                onClick={handleCopy}
                style={{
                  padding: "6px 16px",
                  fontSize: "12px",
                  fontWeight: 700,
                  color: copied ? "#0a0a0f" : "#00c864",
                  background: copied
                    ? "linear-gradient(135deg, #00c864, #00e676)"
                    : "rgba(0,200,100,0.1)",
                  border: copied ? "none" : "1px solid rgba(0,200,100,0.3)",
                  borderRadius: "6px",
                  cursor: "pointer",
                  transition: "all 0.2s",
                  letterSpacing: "0.5px",
                }}
              >
                {copied ? "✅ Copied!" : "📋 Copy All"}
              </button>
            </div>

            <div
              ref={outputRef}
              style={{
                background: "rgba(0,0,0,0.5)",
                border: "1px solid rgba(0,200,100,0.15)",
                borderRadius: "8px",
                padding: "20px",
                fontSize: "14px",
                lineHeight: "2",
                fontFamily: "monospace",
                whiteSpace: "pre-wrap",
                wordBreak: "break-word",
                color: "#e8e0d4",
                maxHeight: "500px",
                overflowY: "auto",
              }}
            >
              {output.split("\n").map((line, i) => {
                if (!line.trim()) return <div key={i} style={{ height: "12px" }} />;

                // Highlight audio tags in orange
                const parts = line.split(/(\[[^\]]+\])/g);
                return (
                  <div key={i}>
                    {parts.map((part, j) => {
                      if (part.match(/^\[.+\]$/)) {
                        return (
                          <span key={j} style={{
                            color: "#ff9500",
                            fontWeight: 600,
                            fontSize: "12px",
                          }}>
                            {part}
                          </span>
                        );
                      }
                      // Highlight CAPITALS
                      const capParts = part.split(/(\b[A-Z]{2,}\b)/g);
                      return capParts.map((cp, k) => {
                        if (cp.match(/^[A-Z]{2,}$/)) {
                          return (
                            <span key={`${j}-${k}`} style={{
                              color: "#ffcc00",
                              fontWeight: 700,
                            }}>
                              {cp}
                            </span>
                          );
                        }
                        return <span key={`${j}-${k}`}>{cp}</span>;
                      });
                    })}
                  </div>
                );
              })}
            </div>

            {/* Settings Reminder */}
            <div style={{
              marginTop: "16px",
              padding: "14px 16px",
              background: "rgba(255,150,0,0.06)",
              border: "1px solid rgba(255,150,0,0.15)",
              borderRadius: "8px",
              fontSize: "12px",
              color: "#8a8090",
              lineHeight: "1.8",
            }}>
              <span style={{ color: "#ff9500", fontWeight: 700 }}>⚙️ ElevenLabs Settings:</span>
              <br />
              Model: <span style={{ color: "#e8e0d4" }}>Eleven V3</span> &nbsp;|&nbsp;
              Voice: <span style={{ color: "#e8e0d4" }}>Deep Hindi Male (V3 optimized)</span> &nbsp;|&nbsp;
              Stability: <span style={{ color: "#e8e0d4" }}>0.45–0.55</span> &nbsp;|&nbsp;
              Clarity: <span style={{ color: "#e8e0d4" }}>0.75</span> &nbsp;|&nbsp;
              Style: <span style={{ color: "#e8e0d4" }}>0.35–0.45</span>
            </div>
          </div>
        )}

        {/* Quick Guide */}
        <div style={{
          background: "rgba(255,255,255,0.02)",
          border: "1px solid rgba(255,255,255,0.06)",
          borderRadius: "12px",
          padding: "20px",
        }}>
          <h3 style={{
            fontSize: "13px",
            fontWeight: 700,
            color: "#ff9500",
            letterSpacing: "1px",
            textTransform: "uppercase",
            marginTop: 0,
            marginBottom: "14px",
          }}>
            📖 How to Use
          </h3>
          <div style={{ fontSize: "13px", lineHeight: "2", color: "#8a8090" }}>
            <div><span style={{ color: "#ffb700" }}>①</span> Paste your full scene script (with 🎬 SCENE headers, 🎙️ NARRATION, 💫 EMOTION)</div>
            <div><span style={{ color: "#ffb700" }}>②</span> Click Generate — Claude reads every scene and builds one V3 prompt</div>
            <div><span style={{ color: "#ffb700" }}>③</span> Copy the output and paste directly into ElevenLabs V3</div>
            <div><span style={{ color: "#ffb700" }}>④</span> Select a deep Hindi male voice from the V3 voice library</div>
            <div style={{ marginTop: "10px", paddingTop: "10px", borderTop: "1px solid rgba(255,255,255,0.06)" }}>
              <span style={{ color: "#ff9500", fontWeight: 600 }}>Supported Tags:</span>{" "}
              <span style={{ color: "#e8e0d4", fontFamily: "monospace", fontSize: "11px" }}>
                [dramatic] [reverent] [heroic] [shouting] [whispers] [pause] [long pause] [sighs] [gasps] [fast-paced] [drawn out] [rising intensity] [sorrowful] [excited] [angry] [calm] [warm] [intense] [ominous] [triumphant] [devotional] [prophetic]
              </span>
            </div>
          </div>
        </div>
      </div>

      <style>{`
        @keyframes spin {
          from { transform: rotate(0deg); }
          to { transform: rotate(360deg); }
        }
        textarea::placeholder {
          color: rgba(255,255,255,0.2);
        }
        textarea:focus {
          border-color: rgba(255,150,0,0.4) !important;
          box-shadow: 0 0 0 2px rgba(255,150,0,0.1);
        }
        button:hover:not(:disabled) {
          transform: translateY(-1px);
          filter: brightness(1.1);
        }
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: rgba(255,150,0,0.3); border-radius: 3px; }
      `}</style>
    </div>
  );
}
