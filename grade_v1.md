# Assignment 2 Grading: nguyenkevin

**Final Score: 0/100 (F)**

## Summary
- Database Models: 0/20
- Task Endpoints: 0/30
- Category Endpoints: 0/15
- Background Tasks: 0/15
- Docker Compose: 0/20

## Detailed Results

### Database Models (0/20)

❌ **DB-01**: Task model has all required fields
   - Score: 0/8
   - Deduction: Cannot test - API not accessible (-8 pts, critical)

❌ **DB-02**: Category model with unique name constraint
   - Score: 0/6
   - Deduction: Cannot test - API not accessible (-6 pts, critical)

❌ **DB-03**: Task-Category relationship (task belongs to category)
   - Score: 0/6
   - Deduction: Cannot test - API not accessible (-6 pts, critical)

### Task Endpoints with Validation (0/30)

❌ **TASK-01**: GET /tasks returns list of all tasks
   - Score: 0/4
   - Deduction: Cannot test - API not accessible (-4 pts, critical)

❌ **TASK-02**: GET /tasks?completed=false filters by completion status
   - Score: 0/4
   - Deduction: Cannot test - API not accessible (-4 pts, critical)

❌ **TASK-03**: GET /tasks/:id returns single task with category info
   - Score: 0/3
   - Deduction: Cannot test - API not accessible (-3 pts, critical)

❌ **TASK-04**: GET /tasks/:id returns 404 when not found
   - Score: 0/2
   - Deduction: Cannot test - API not accessible (-2 pts, critical)

❌ **TASK-05**: POST /tasks creates task, returns 201
   - Score: 0/4
   - Deduction: Cannot test - API not accessible (-4 pts, critical)

❌ **TASK-06**: POST /tasks validates input (title required, length limits)
   - Score: 0/4
   - Deduction: Cannot test - API not accessible (-4 pts, critical)

❌ **TASK-07**: Validation errors include structured messages
   - Score: 0/2
   - Deduction: Cannot test - API not accessible (-2 pts, critical)

❌ **TASK-08**: PUT /tasks/:id updates task, returns 200
   - Score: 0/3
   - Deduction: Cannot test - API not accessible (-3 pts, critical)

❌ **TASK-09**: PUT /tasks/:id returns 404 when not found
   - Score: 0/1
   - Deduction: Cannot test - API not accessible (-1 pts, critical)

❌ **TASK-10**: DELETE /tasks/:id deletes task, returns 200 with message
   - Score: 0/2
   - Deduction: Cannot test - API not accessible (-2 pts, critical)

❌ **TASK-11**: DELETE /tasks/:id returns 404 when not found
   - Score: 0/1
   - Deduction: Cannot test - API not accessible (-1 pts, critical)

### Category Endpoints (0/15)

❌ **CAT-01**: GET /categories returns categories with task_count
   - Score: 0/5
   - Deduction: Cannot test - API not accessible (-5 pts, critical)

❌ **CAT-02**: GET /categories/:id returns category with its tasks
   - Score: 0/3
   - Deduction: Cannot test - API not accessible (-3 pts, critical)

❌ **CAT-03**: POST /categories validates unique name and hex color
   - Score: 0/4
   - Deduction: Cannot test - API not accessible (-4 pts, critical)

❌ **CAT-04**: DELETE /categories/:id prevents deletion with existing tasks
   - Score: 0/3
   - Deduction: Cannot test - API not accessible (-3 pts, critical)

### Background Task Processing (0/15)

❌ **BG-01**: Redis and rq worker properly configured
   - Score: 0/4
   - Deduction: No docker-compose.yml (-4 pts, critical)

❌ **BG-02**: notification_queued: true when due_date within 24h
   - Score: 0/5
   - Deduction: Cannot test - API not accessible (-5 pts, critical)

❌ **BG-03**: notification_queued: false when no due_date or > 24h
   - Score: 0/3
   - Deduction: Cannot test - API not accessible (-3 pts, critical)

❌ **BG-04**: Background job executes (worker logs show reminder)
   - Score: 0/3
   - Deduction: No docker-compose.yml (-3 pts, critical)

### Docker Compose (0/20)

❌ **DOCK-01**: docker-compose.yml defines all 4 services (app, db, redis, worker)
   - Score: 0/5
   - Deduction: No docker-compose.yml found (-5 pts, critical)

❌ **DOCK-02**: docker-compose up --build runs without errors
   - Score: 0/8
   - Deduction: No docker-compose.yml to build (-8 pts, critical)

❌ **DOCK-03**: All services connect properly (app to db+redis, worker to redis)
   - Score: 0/4
   - Deduction: Cannot test - API not accessible (-4 pts, critical)

❌ **DOCK-04**: API is accessible and functional on configured port
   - Score: 0/3
   - Deduction: API not accessible (-3 pts, critical)

## Strengths
- N/A

## Areas for Improvement
- docker-compose.yml defines all 4 services (app, db, redis, worker): No docker-compose.yml found
- Redis and rq worker properly configured: No docker-compose.yml
- docker-compose up --build runs without errors: No docker-compose.yml to build
- All services connect properly (app to db+redis, worker to redis): Cannot test - API not accessible
- API is accessible and functional on configured port: API not accessible
- Task model has all required fields: Cannot test - API not accessible
- Category model with unique name constraint: Cannot test - API not accessible
- Task-Category relationship (task belongs to category): Cannot test - API not accessible
- GET /tasks returns list of all tasks: Cannot test - API not accessible
- GET /tasks?completed=false filters by completion status: Cannot test - API not accessible
- GET /tasks/:id returns single task with category info: Cannot test - API not accessible
- GET /tasks/:id returns 404 when not found: Cannot test - API not accessible
- POST /tasks creates task, returns 201: Cannot test - API not accessible
- POST /tasks validates input (title required, length limits): Cannot test - API not accessible
- Validation errors include structured messages: Cannot test - API not accessible
- PUT /tasks/:id updates task, returns 200: Cannot test - API not accessible
- PUT /tasks/:id returns 404 when not found: Cannot test - API not accessible
- DELETE /tasks/:id deletes task, returns 200 with message: Cannot test - API not accessible
- DELETE /tasks/:id returns 404 when not found: Cannot test - API not accessible
- GET /categories returns categories with task_count: Cannot test - API not accessible
- GET /categories/:id returns category with its tasks: Cannot test - API not accessible
- POST /categories validates unique name and hex color: Cannot test - API not accessible
- DELETE /categories/:id prevents deletion with existing tasks: Cannot test - API not accessible
- notification_queued: true when due_date within 24h: Cannot test - API not accessible
- notification_queued: false when no due_date or > 24h: Cannot test - API not accessible
- Background job executes (worker logs show reminder): No docker-compose.yml
