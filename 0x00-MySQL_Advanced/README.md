# 0x00. MySQL Advanced

This project practices **advanced MySQL**: unique constraints, grouping, triggers, stored procedures, and validation so the database enforces rules and keeps data consistent.

---

## What does each file do?

Each answer is the **problem the file solves** and how to run it.

---

### **What does `0-uniq_users.sql` do?**  
It creates a `users` table with a **unique constraint on email** so the same email cannot be stored twice. You practice defining a table with `UNIQUE`.  
**Run:** `mysql -u root -p < 0-uniq_users.sql` (or paste in MySQL client).

### **What does `1-country_users.sql` do?**  
It creates or alters a users table to include a **country** attribute so you can store and query users by country.  
**Run:** Load in MySQL after any required schema.

### **What does `2-fans.sql` do?**  
It **ranks band origins by total number of fans**: groups rows from a `metal_bands` (or similar) table by `origin`, sums `fans`, and orders by that sum descending.  
**Run:** `mysql -u root -p mydb < 2-fans.sql` (ensure the bands table exists).

### **What does `3-glam_rock.sql` do?**  
It **lists glam rock bands** (e.g. those formed between 1969 and 1972) and shows lifespan. You practice `WHERE` with date/range conditions.  
**Run:** Execute against a database that has the bands table.

### **What does `4-init.sql` do?**  
It creates the **schema for a store**: typically tables for items (with quantity) and orders. Used as the base before running `4-store.sql`.  
**Run:** Load first: `mysql -u root -p mydb < 4-init.sql`.

### **What does `4-store.sql` do?**  
It defines a **trigger** that runs when a new order is inserted: it **decreases the item quantity** in the items table so stock stays consistent.  
**Run:** Load after `4-init.sql`.

### **What does `5-init.sql` do?**  
It creates the **users table** used by the valid_email trigger (e.g. id, email). Load before `5-valid_email.sql`.  
**Run:** `mysql -u root -p mydb < 5-init.sql`.

### **What does `5-valid_email.sql` do?**  
It defines a **trigger** that runs before an update on users: if the new email is invalid, it **resets the email to NULL** (or keeps the old value) so invalid emails are never stored.  
**Run:** Load after `5-init.sql`.

### **What does `6-init.sql` do?**  
It creates the **schema for the bonus/project** task (tables required for the bonus stored procedure).  
**Run:** Load before `6-bonus.sql`.

### **What does `6-bonus.sql` do?**  
It defines a **stored procedure** that adds a bonus (e.g. updates a project or correction table). You practice writing and calling procedures.  
**Run:** Load after `6-init.sql`; then call the procedure from the MySQL client.

### **What does `7-init.sql` do?**  
It creates the **schema for users and corrections** (or similar) used by the average score procedure.  
**Run:** Load before `7-average_score.sql`.

### **What does `7-average_score.sql` do?**  
It defines a **stored procedure** that **computes and stores the average score** for a user (e.g. from a corrections or projects table).  
**Run:** Load after `7-init.sql`; then call the procedure.

---

## How to do the exercises yourself

1. Create a database and load the relevant `*-init.sql` when a task depends on it.
2. Run the task script (e.g. `mysql -u root -p mydb < 2-fans.sql` or paste in MySQL client).
3. For triggers: ensure the table and column names match the spec; test by inserting/updating and checking the result.
