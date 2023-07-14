-- sql script that lists all bands with Glam rock as their main style, ranked by their longevity

-- statement declaration
SELECT band_name, COALESCE(split, 2022) - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%';
