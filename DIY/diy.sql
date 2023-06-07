SELECT transistors FROM computer.video_card

UPDATE computer.video_card
SET process_size = REPLACE(process_size, 'nm', '纳米')
WHERE process_size LIKE '%nm%';


UPDATE computer.video_card
SET transistors = REPLACE(transistors, ',', '')
WHERE transistors LIKE '%,%';

UPDATE computer.video_card
SET transistors = CONCAT(SUBSTRING(transistors, 1, LENGTH(transistors) - 2), '亿');


UPDATE computer.video_card
SET transistors = REPLACE(transistors, '亿', ' 亿')