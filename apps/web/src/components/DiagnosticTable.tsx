import React from 'react';

export function DiagnosticTable({ records }: { records: any[] }) {
  return (
    <div style={{ background: '#fff', padding: '1.5rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
      <h3 style={{ margin: '0 0 1rem 0', color: '#0f172a' }}>📋 Diagnostic History Log</h3>
      {records.length === 0 ? (
        <p style={{ color: '#64748b', fontSize: '14px' }}>No crop diagnostic records available.</p>
      ) : (
        <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '14px' }}>
          <thead>
            <tr style={{ background: '#f8fafc', textAlign: 'left', borderBottom: '2px solid #e2e8f0' }}>
              <th style={{ padding: '0.75rem' }}>Farmer ID</th>
              <th style={{ padding: '0.75rem' }}>Crop</th>
              <th style={{ padding: '0.75rem' }}>Diagnosis</th>
              <th style={{ padding: '0.75rem' }}>Treatment Directive</th>
            </tr>
          </thead>
          <tbody>
            {records.map((r, i) => (
              <tr key={i} style={{ borderBottom: '1px solid #e2e8f0' }}>
                <td style={{ padding: '0.75rem', fontWeight: 'bold' }}>{r.farmer_id}</td>
                <td style={{ padding: '0.75rem' }}>{r.crop_type}</td>
                <td style={{ padding: '0.75rem', color: '#15803d', fontWeight: 'bold' }}>{r.diagnosis}</td>
                <td style={{ padding: '0.75rem' }}>{r.recommended_treatment || 'Apply Propiconazole fungicide at 0.5L/ha'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
