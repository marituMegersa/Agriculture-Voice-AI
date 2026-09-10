import React from 'react';

export function SoilFertilizerCalculator({ result }: { result: any }) {
  if (!result) return null;

  return (
    <div style={{ marginTop: '1.5rem', padding: '1.5rem', background: '#f0fdf4', border: '1px solid #bbf7d0', borderRadius: '8px' }}>
      <h4 style={{ margin: 0, color: '#166534' }}>Diagnostic Result: {result.diagnosis} ({result.confidence})</h4>
      <p style={{ color: '#15803d', marginTop: '0.5rem' }}><strong>Treatment Directive:</strong> {result.recommendedTreatment}</p>
      <div style={{ marginTop: '1rem', borderTop: '1px solid #86efac', paddingTop: '0.75rem' }}>
        <strong style={{ fontSize: '12px', color: '#166534' }}>Recommended Fertilizer Dosage:</strong>
        <p style={{ margin: '0.25rem 0 0 0', color: '#14532d', fontWeight: 'bold' }}>{result.fertilizerDosage}</p>
      </div>
    </div>
  );
}
