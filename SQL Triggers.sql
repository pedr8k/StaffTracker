-- Trigger para registrar novas escalas adicionadas
CREATE TRIGGER IF NOT EXISTS trg_insert_escala
AFTER INSERT ON escala
FOR EACH ROW
BEGIN
    INSERT INTO historico (funcionario_id, plantao_id, acao)
    VALUES (NEW.funcionario_id, NEW.plantao_id, 'Adicionado');
END;

-- Trigger para registrar alterações em escalas existentes
CREATE TRIGGER IF NOT EXISTS trg_update_escala
AFTER UPDATE ON escala
FOR EACH ROW
BEGIN
    INSERT INTO historico (funcionario_id, plantao_id, acao)
    VALUES (NEW.funcionario_id, NEW.plantao_id, 'Alterado');
END;

-- Trigger para registrar exclusões de escalas
CREATE TRIGGER IF NOT EXISTS trg_delete_escala
AFTER DELETE ON escala
FOR EACH ROW
BEGIN
    INSERT INTO historico (funcionario_id, plantao_id, acao)
    VALUES (OLD.funcionario_id, OLD.plantao_id, 'Removido');
END;