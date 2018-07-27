#!/bin/bash

set -e

bzcat 段落對齊/段落對齊.sql.bz2 > a.sql
echo "SELECT * FROM dic_can ORDER BY id;" >> a.sql
cat a.sql | \
  sed '/^SET/d' | \
  sed '/^COMMENT/d' | \
  sed '/^ALTER TABLE/d' | \
  sed '/SCHEMA/,+5d' | \
  sed '/SEQUENCE/d' | \
  
  sqlite3 -header -csv | \
  cat > dict.csv

echo 'Tī dict.csv.'
  sed '/ALTER TABLE/{N;d;}' | \