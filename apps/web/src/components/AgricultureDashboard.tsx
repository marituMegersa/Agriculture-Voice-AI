import React from 'react';

export function AgricultureDashboard({ total }: { total: number }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '1rem', marginBottom: '1.5rem' }}>
      <div style={{ background: '#fff', padding: '1.25rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
        <div style={{ fontSize: '12px', color: '#64748b', fontWeight: 'bold' }}>FARMERS ADVISED</div>
        <div style={{ fontSize: '24px', fontWeight: 'bold', color: '#0f172a', marginTop: '0.25rem' }}>{total}</div>
      </div>
      <div style={{ background: '#fff', padding: '1.25rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
        <div style={{ fontSize: '12px', color: '#64748b', fontWeight: 'bold' }}>LANGUAGES SUPPORTED</div>
        <div style={{ fontSize: '24px', fontWeight: 'bold', color: '#16a34a', marginTop: '0.25rem' }}>Amharic / Afaan Oromo</div>
      </div>
      <div style={{ background: '#fff', padding: '1.25rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
        <div style={{ fontSize: '12px', color: '#64748b', fontWeight: 'bold' }}>SYSTEM ACCURACY</div>
        <div style={{ fontSize: '24px', fontWeight: 'bold', color: '#059669', marginTop: '0.25rem' }}>94.2%</div>
      </div>
    </div>
  );
}
