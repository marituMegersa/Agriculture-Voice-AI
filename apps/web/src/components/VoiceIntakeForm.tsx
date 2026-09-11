import React, { useState } from 'react';

export function VoiceIntakeForm({ onSubmit }: { onSubmit: (data: any) => void }) {
  const [farmerId, setFarmerId] = useState('FARMER-8831');
  const [crop, setCrop] = useState('Wheat');
  const [transcript, setTranscript] = useState('እህሌ ቢጫ ዝገት ምልክት አሳይቷል');
  const [lang, setLang] = useState('Amharic');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit({
      farmer_id: farmerId,
      crop_type: crop,
      voice_transcript: transcript,
      language: lang
    });
  };

  return (
    <form onSubmit={handleSubmit} style={{ background: '#fff', padding: '1.5rem', borderRadius: '8px', border: '1px solid #e2e8f0', marginBottom: '1.5rem' }}>
      <h3 style={{ margin: '0 0 1rem 0', color: '#0f172a' }}>🎙️ Voice Crop Diagnostic Intake</h3>
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
        <div>
          <label style={{ fontSize: '12px', fontWeight: 'bold' }}>Farmer Reference ID</label>
          <input value={farmerId} onChange={e => setFarmerId(e.target.value)} required style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1' }} />
        </div>
        <div>
          <label style={{ fontSize: '12px', fontWeight: 'bold' }}>Crop Type</label>
          <input value={crop} onChange={e => setCrop(e.target.value)} required style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1' }} />
        </div>
        <div>
          <label style={{ fontSize: '12px', fontWeight: 'bold' }}>Speech Language</label>
          <select value={lang} onChange={e => setLang(e.target.value)} style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1' }}>
            <option value="Amharic">Amharic (አማርኛ)</option>
            <option value="Afaan Oromo">Afaan Oromo</option>
            <option value="English">English</option>
          </select>
        </div>
      </div>
      <div style={{ marginTop: '1rem' }}>
        <label style={{ fontSize: '12px', fontWeight: 'bold' }}>Transcribed Speech Query</label>
        <textarea value={transcript} onChange={e => setTranscript(e.target.value)} required style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1', height: '60px' }} />
      </div>
      <button type="submit" style={{ marginTop: '1rem', background: '#16a34a', color: '#fff', padding: '0.75rem 1.5rem', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold' }}>
        Run Voice Diagnostic
      </button>
    </form>
  );
}
