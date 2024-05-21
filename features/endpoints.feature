Feature: Testando endpoints para gerar e atualizar pagamento

  Scenario: Gerar um pagamento com sucesso
    Given que eu tenho os dados para gerar um pagamento
    When eu faço uma solicitação para gerar um pagamento
    Then a resposta deve conter um código de status 200
    And o pagamento deve ser gerado com sucesso

  Scenario: Atualizar um pagamento com sucesso
    Given que eu tenho os dados para atualizar um pagamento
    When eu faço uma solicitação para atualizar um pagamento
    Then a resposta deve conter um código de status 200
    And o pagamento deve ser atualizado com sucesso

  Scenario: Tentar atualizar um pagamento com dados inválidos
    Given que eu tenho dados inválidos para atualizar um pagamento
    When eu faço uma solicitação para atualizar um pagamento
    Then a resposta deve conter um código de status 400
    And uma mensagem de erro deve ser retornada

  Scenario: Tentar gerar um pagamento com dados incompletos
    Given que eu tenho dados incompletos para gerar um pagamento
    When eu faço uma solicitação para gerar um pagamento
    Then a resposta deve conter um código de status 400
    And uma mensagem de erro deve ser retornada

  Scenario: Tentar atualizar um pagamento com um metodo nao permitido
    Given que eu tenho os dados para atualizar um pagamento
    When eu faço uma solicitação get nao permmitida para atualizar um pagamento
    Then a resposta deve conter um código de status 405
    And uma mensagem de erro deve ser retornada

  Scenario: Tentar gerar um pagamento com um metodo nao permitido
    Given que eu tenho os dados para gerar um pagamento
    When eu faço uma solicitação get nao permitida para gerar um pagamento
    Then a resposta deve conter um código de status 405
    And uma mensagem de erro deve ser retornada  