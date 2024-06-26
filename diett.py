import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# إنشاء الجداول إذا لم تكن موجودة
cursor.execute('''
CREATE TABLE IF NOT EXISTS weight_loss_diet (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day TEXT NOT NULL,
    meal1 TEXT NOT NULL,
    meal2 TEXT NOT NULL,
    meal3 TEXT NOT NULL,
    snack TEXT NOT NULL,
    calories INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS weight_gain_diet (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day TEXT NOT NULL,
    meal1 TEXT NOT NULL,
    meal2 TEXT NOT NULL,
    meal3 TEXT NOT NULL,
    snack TEXT NOT NULL,
    calories INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS muscle_cutting_diet (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day TEXT NOT NULL,
    meal1 TEXT NOT NULL,
    meal2 TEXT NOT NULL,
    meal3 TEXT NOT NULL,
    snack TEXT NOT NULL,
    calories INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS muscle_bulking_diet (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day TEXT NOT NULL,
    meal1 TEXT NOT NULL,
    meal2 TEXT NOT NULL,
    meal3 TEXT NOT NULL,
    snack TEXT NOT NULL,
    calories INTEGER NOT NULL
)
''')

# بيانات وهمية للنظام الغذائي لمدة 14 يوم
weight_loss_data = [
    ('السبت', 'شوفان مع فواكه', 'سلطة تونة', 'دجاج مشوي مع خضار', 'مكسرات', 1500),
    ('الأحد', 'زبادي مع فواكه', 'سمك مشوي مع أرز بني', 'لحم مشوي مع سلطة', 'تفاح', 1500),
    ('الإثنين', 'بيض مسلوق مع خضار', 'دجاج مع أرز بني', 'سلطة خضار', 'موز', 1500),
    ('الثلاثاء', 'شوفان مع لبن', 'لحم مع خضار', 'دجاج مشوي مع سلطة', 'برتقال', 1500),
    ('الأربعاء', 'فطائر صحية', 'سلطة تونة', 'سمك مع خضار', 'جزر', 1500),
    ('الخميس', 'بيض مع خبز', 'لحم مشوي مع خضار', 'سلطة خضراء', 'تفاح', 1500),
    ('الجمعة', 'شوفان مع عسل', 'دجاج مع بطاطا', 'سمك مع أرز بني', 'موز', 1500),
    ('السبت', 'زبادي مع فواكه', 'سلطة تونة', 'دجاج مشوي مع خضار', 'مكسرات', 1500),
    ('الأحد', 'بيض مسلوق مع خضار', 'سمك مشوي مع أرز بني', 'لحم مشوي مع سلطة', 'تفاح', 1500),
    ('الإثنين', 'شوفان مع لبن', 'دجاج مع أرز بني', 'سلطة خضار', 'موز', 1500),
    ('الثلاثاء', 'زبادي مع مكسرات', 'لحم مع خضار', 'دجاج مشوي مع سلطة', 'برتقال', 1500),
    ('الأربعاء', 'شوفان مع عسل', 'سلطة تونة', 'سمك مع خضار', 'جزر', 1500),
    ('الخميس', 'بيض مع خبز', 'لحم مشوي مع خضار', 'سلطة خضراء', 'تفاح', 1500),
    ('الجمعة', 'زبادي مع فواكه', 'دجاج مع بطاطا', 'سمك مع أرز بني', 'موز', 1500)
]

weight_gain_data = [
    ('السبت', 'بيض مع خبز', 'دجاج مع أرز', 'لحم مع بطاطس', 'موز', 2500),
    ('الأحد', 'شوفان مع حليب', 'سمك مع معكرونة', 'ستيك مع خضار', 'تمر', 2500),
    ('الإثنين', 'زبادي مع عسل', 'لحم مع أرز', 'دجاج مع بطاطا', 'تفاح', 2500),
    ('الثلاثاء', 'فطائر محشوة', 'سمك مع بطاطا', 'دجاج مع معكرونة', 'برتقال', 2500),
    ('الأربعاء', 'بيض مسلوق', 'لحم مع خضار', 'سمك مع أرز', 'موز', 2500),
    ('الخميس', 'شوفان مع فواكه', 'دجاج مع بطاطا', 'لحم مع معكرونة', 'تمر', 2500),
    ('الجمعة', 'زبادي مع مكسرات', 'سمك مع أرز', 'دجاج مع بطاطا', 'تفاح', 2500),
    ('السبت', 'بيض مع خبز', 'دجاج مع أرز', 'لحم مع بطاطس', 'موز', 2500),
    ('الأحد', 'شوفان مع حليب', 'سمك مع معكرونة', 'ستيك مع خضار', 'تمر', 2500),
    ('الإثنين', 'زبادي مع عسل', 'لحم مع أرز', 'دجاج مع بطاطا', 'تفاح', 2500),
    ('الثلاثاء', 'فطائر محشوة', 'سمك مع بطاطا', 'دجاج مع معكرونة', 'برتقال', 2500),
    ('الأربعاء', 'بيض مسلوق', 'لحم مع خضار', 'سمك مع أرز', 'موز', 2500),
    ('الخميس', 'شوفان مع فواكه', 'دجاج مع بطاطا', 'لحم مع معكرونة', 'تمر', 2500),
    ('الجمعة', 'زبادي مع مكسرات', 'سمك مع أرز', 'دجاج مع بطاطا', 'تفاح', 2500)
]

muscle_cutting_data = [
    ('السبت', 'بيض مسلوق', 'تونة مع سلطة', 'دجاج مشوي مع خضار', 'خيار', 1800),
    ('الأحد', 'زبادي مع لوز', 'سمك مشوي', 'لحم مشوي مع سلطة', 'جزر', 1800),
    ('الإثنين', 'شوفان مع حليب', 'دجاج مع خضار', 'سمك مع سلطة', 'تفاح', 1800),
    ('الثلاثاء', 'زبادي مع فواكه', 'تونة مع خضار', 'لحم مع أرز بني', 'موز', 1800),
    ('الأربعاء', 'بيض مع خبز', 'سمك مع خضار', 'دجاج مع سلطة', 'برتقال', 1800),
    ('الخميس', 'شوفان مع لبن', 'لحم مع خضار', 'سمك مع سلطة', 'جزر', 1800),
    ('الجمعة', 'زبادي مع عسل', 'تونة مع أرز بني', 'دجاج مع بطاطا', 'مكسرات', 1800),
    ('السبت', 'بيض مسلوق', 'تونة مع سلطة', 'دجاج مشوي مع خضار', 'خيار', 1800),
    ('الأحد', 'زبادي مع لوز', 'سمك مشوي', 'لحم مشوي مع سلطة', 'جزر', 1800),
    ('الإثنين', 'شوفان مع حليب', 'دجاج مع خضار', 'سمك مع سلطة', 'تفاح', 1800),
    ('الثلاثاء', 'زبادي مع فواكه', 'تونة مع خضار', 'لحم مع أرز بني', 'موز', 1800),
    ('الأربعاء', 'بيض مع خبز', 'سمك مع خضار', 'دجاج مع سلطة', 'برتقال', 1800),
    ('الخميس', 'شوفان مع لبن', 'لحم مع خضار', 'سمك مع سلطة', 'جزر', 1800),
    ('الجمعة', 'زبادي مع عسل', 'تونة مع أرز بني', 'دجاج مع بطاطا', 'مكسرات', 1800)
]

muscle_bulking_data = [
    ('السبت', 'بان كيك مع عسل', 'دجاج مع أرز', 'ستيك مع بطاطس', 'زبادي', 3000),
    ('الأحد', 'شوفان مع حليب', 'سمك مع معكرونة', 'لحم مع بطاطس', 'مكسرات', 3000),
    ('الإثنين', 'فطائر محشوة', 'دجاج مع خضار', 'سمك مع أرز', 'تمر', 3000),
    ('الثلاثاء', 'بيض مسلوق', 'لحم مع بطاطس', 'دجاج مع معكرونة', 'موز', 3000),
    ('الأربعاء', 'زبادي مع عسل', 'سمك مع خضار', 'لحم مع أرز', 'تفاح', 3000),
    ('الخميس', 'شوفان مع مكسرات', 'دجاج مع بطاطا', 'سمك مع خضار', 'جزر', 3000),
    ('الجمعة', 'بيض مع خبز', 'لحم مع خضار', 'دجاج مع أرز', 'برتقال', 3000),
    ('السبت', 'بان كيك مع عسل', 'دجاج مع أرز', 'ستيك مع بطاطس', 'زبادي', 3000),
    ('الأحد', 'شوفان مع حليب', 'سمك مع معكرونة', 'لحم مع بطاطس', 'مكسرات', 3000),
    ('الإثنين', 'فطائر محشوة', 'دجاج مع خضار', 'سمك مع أرز', 'تمر', 3000),
    ('الثلاثاء', 'بيض مسلوق', 'لحم مع بطاطس', 'دجاج مع معكرونة', 'موز', 3000),
    ('الأربعاء', 'زبادي مع عسل', 'سمك مع خضار', 'لحم مع أرز', 'تفاح', 3000),
    ('الخميس', 'شوفان مع مكسرات', 'دجاج مع بطاطا', 'سمك مع خضار', 'جزر', 3000),
    ('الجمعة', 'بيض مع خبز', 'لحم مع خضار', 'دجاج مع أرز', 'برتقال', 3000)
]

# إدخال البيانات
for data in weight_loss_data:
    cursor.execute("INSERT INTO weight_loss_diet (day, meal1, meal2, meal3, snack, calories) VALUES (?, ?, ?, ?, ?, ?)", data)

for data in weight_gain_data:
    cursor.execute("INSERT INTO weight_gain_diet (day, meal1, meal2, meal3, snack, calories) VALUES (?, ?, ?, ?, ?, ?)", data)

for data in muscle_cutting_data:
    cursor.execute("INSERT INTO muscle_cutting_diet (day, meal1, meal2, meal3, snack, calories) VALUES (?, ?, ?, ?, ?, ?)", data)

for data in muscle_bulking_data:
    cursor.execute("INSERT INTO muscle_bulking_diet (day, meal1, meal2, meal3, snack, calories) VALUES (?, ?, ?, ?, ?, ?)", data)

conn.commit()
conn.close()
