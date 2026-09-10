import React, { useState } from 'react';

export function VoiceIntakeAdvisor({ onDiagnose }: { onDiagnose: (res: any) => void }) {
  const [language, setLanguage] = useState('Amharic');
  const [transcript, setTranscript] = useState('እህሌ ቢጫ ዝገት ምልክት አሳይቷል (My crop shows yellow rust symptoms)');

  const handleSimulateVoice = () => {
    onDiagnose({
      language,
      transcript,
      diagnosis: 'Yellow Rust (Puccinia striiformis)',
      confidence: '94%',
      recommendedTreatment: 'Apply Propiconazole fungicide at 0.5L/ha. Ensure proper field drainage.',
      fertilizerDosage: 'Urea: 100 kg/ha, DAP: 50 kg/ha'
    });
  };

  return (
    <div style={{ background: '#ffffff', padding: '1.5rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
      <h3 style={{ color: '#0f172a', marginBottom: '1rem' }}>🗣️ Multilingual Voice Crop Intake</h3>
      <div style={{ marginBottom: '1rem' }}>
        <label style={{ fontSize: '12px', fontWeight: 'bold' }}>Input Language</label>
        <select value={language} onChange={e => setLanguage(e.target.value)} style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1' }}>
          <option value="Amharic">Amharic (አማርኛ)</option>
          <option value="Afaan Oromo">Afaan Oromo</option>
          <option value="English">English</option>
        </select>
      </div>
      <div>
        <label style={{ fontSize: '12px', fontWeight: 'bold' }}>Speech Transcribed Input</label>
        <textarea value={transcript} onChange={e => setTranscript(e.target.value)} style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1', height: '70px' }} />
      </div>
      <button onClick={handleSimulateVoice} style={{ marginTop: '1rem', background: '#16a34a', color: '#fff', padding: '0.75rem 1.5rem', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold' }}>
        🎙️ Process Voice Diagnostic
      </button>
    </div>
  );
}
