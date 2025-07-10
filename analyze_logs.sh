#!/bin/bash

{
    echo "Отчет о логе веб-сервера"
    echo "========================"

    # 1) Общее количество запросов
    echo "Общее количество запросов: $(wc -l < access.log)"

    # 2) количество уникальных IP-адресов
    echo "Количество уникальных IP-адресов: $(awk '{ids[$1]++} END {print length(ids)}' access.log)"
    echo ""

    # 3) Количество запросов по методам
    echo "Количество запросов по методам:"
    awk '
    {
    method = substr($6, 2)
    methods[method]++
    }
    END {
    for (m in methods)
        printf "%d %s\n", methods[m], m
    }' access.log
    echo ""

    # 4) самый популярный URL
    echo "Самый популярный URL: $(awk '
    {
        urls[$7]++
    }
    END {
        max = 0
        p_url = ""
        for (u in urls) {
            if (urls[u] > max) {
                max = urls[u]
                p_url = u
            }
        }
        printf "%d %s", max, p_url
    }' access.log)"
} > report.txt