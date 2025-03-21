-- Índice para a tabela funcionarios, buscando por nome rapidamente
CREATE INDEX IF NOT EXISTS idx_funcionarios_nome ON funcionarios(nome);

-- Índice para a tabela escala, buscando rapidamente pelo funcionario_id
CREATE INDEX IF NOT EXISTS idx_escala_funcionario ON escala(funcionario_id);

-- Índice para a tabela escala, buscando rapidamente pelo plantao_id
CREATE INDEX IF NOT EXISTS idx_escala_plantao ON escala(plantao_id);