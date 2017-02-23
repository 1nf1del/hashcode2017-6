# Algorithms

## Basic (output)

Score: 1963176

```
select endpoint with highest latency
    select video with highest views
        select cache with least latency
```

## Improvement 1 (output2)

Score: 1971139
```
select endpoint with highest latency (weight = latency x number of requests)
    select video with highest views
        select cache with least latency
```


## Improvement 2(output3)

Score: 1961999

```
select endpoint with highest latency [weight = (data_center_latency - avg_cache_latency) x number of requests]
    select video with highest views
        select cache with least latency
```
