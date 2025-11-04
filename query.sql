-- Query di esempio per inserire un preventivo
INSERT INTO preventivi (
    tipo,
    codice,
    descrizione,
    unitaMisura,
    quantita,
    prezzoUnitario,
    prezzoTotale,
    MRprezzoUnitario,
    MRprezzoTotale,
    MRricarico,
    manoRprezzoUnitario,
    manoRprezzoTotale,
    manoRricarico,
    PMprezzoUnitario,
    PMprezzoTotale,
    CMprezzoUnitario,
    CMprezzoTotale
) VALUES (
    1.0,                    -- tipo (REAL)
    1001,                   -- codice (INTEGER)
    'Installazione Caldaia Murale 24kW', -- descrizione (TEXT)
    'PZ',                   -- unitaMisura (TEXT)
    1.0,                    -- quantita (REAL)
    800.00,                 -- prezzoUnitario (REAL)
    800.00,                 -- prezzoTotale (prezzoUnitario * quantita)
    920.00,                 -- MRprezzoUnitario (REAL)
    920.00,                 -- MRprezzoTotale (MRprezzoUnitario * quantita)
    15,                     -- MRricarico (INTEGER) - percentuale di ricarico
    200.00,                 -- manoRprezzoUnitario (REAL)
    200.00,                 -- manoRprezzoTotale (manoRprezzoUnitario * quantita)
    25.0,                   -- manoRricarico (REAL) - percentuale di ricarico
    1120.00,               -- PMprezzoUnitario (REAL) - Prezzo Materiale (MR + manoR)
    1120.00,               -- PMprezzoTotale (PMprezzoUnitario * quantita)
    1400.00,               -- CMprezzoUnitario (REAL) - Costo Materiale finale
    1400.00                 -- CMprezzoTotale (CMprezzoUnitario * quantita)
);
