{% set apples = ["Gala", "Fuji", "McIntosh"] %}

{% for i in apples %}
    {% if i != "MacIntosh" %}
        {{i}}
    {%else%}
        I hate {{i}}
    {%endif%}
{%endfor%}