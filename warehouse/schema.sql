CREATE TABLE IF NOT EXISTS receipts(batch_id VARCHAR PRIMARY KEY, signature VARCHAR NOT NULL, inserted INTEGER NOT NULL);
CREATE TABLE IF NOT EXISTS source_rows(table_name VARCHAR, row_key VARCHAR, payload VARCHAR NOT NULL, batch_id VARCHAR NOT NULL, PRIMARY KEY(table_name,row_key));
        CREATE TABLE IF NOT EXISTS products(sku VARCHAR PRIMARY KEY, pack_size DECIMAL(18,4), label VARCHAR);
        CREATE TABLE IF NOT EXISTS movements(movement_id VARCHAR PRIMARY KEY, warehouse VARCHAR, sku VARCHAR, occurred_at VARCHAR, quantity DECIMAL(18,4), unit VARCHAR, kind VARCHAR);
        CREATE TABLE IF NOT EXISTS counts(count_id VARCHAR PRIMARY KEY, warehouse VARCHAR, sku VARCHAR, cutoff_at VARCHAR, quantity DECIMAL(18,4));
        CREATE TABLE IF NOT EXISTS transfers(transfer_id VARCHAR PRIMARY KEY, source VARCHAR, destination VARCHAR, sku VARCHAR, dispatched_at VARCHAR, quantity DECIMAL(18,4), status VARCHAR);
        CREATE TABLE IF NOT EXISTS arrivals(arrival_id VARCHAR PRIMARY KEY, transfer_id VARCHAR, received_at VARCHAR, quantity DECIMAL(18,4), disposition VARCHAR);

CREATE TABLE IF NOT EXISTS stock_alerts(alert_id VARCHAR PRIMARY KEY, warehouse VARCHAR, sku VARCHAR, reason VARCHAR, quantity DECIMAL(18,4));