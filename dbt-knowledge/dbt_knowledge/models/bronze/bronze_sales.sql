{{
  config(
    materialized = 'view',
    )
}} 
{# block config #}

SELECT 
    *
FROM
    {{ source('source', 'fact_sales') }}