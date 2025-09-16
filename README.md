## System Architecture Overview
### Design
https://excalidraw.com/#json=6eTyIoPxZGizmH7NwBDoL,QccDsvQLxCB9UMT39pRrhw

### Core Components

#### 1. Client Layer
- **Web/Mobile Clients**: User interfaces that interact with the system through a single API gateway
- **SSE (Server-Sent Events)**: Enables real-time notifications for drop alerts, stock updates, and order confirmations

#### 2. API Gateway
- **Single Entry Point**: All client requests route through this centralized gateway
- **Rate Limiter**: Protects backend services from excessive traffic and DDoS attacks
- **Authentication**: Handles user authorization before forwarding requests to internal services
- **API Composition**: Aggregates data from multiple services to reduce client-side network calls

#### 3. Microservices Architecture
The system decomposes functionality into specialized services:

- **Creator Service**: Manages creator profiles, product creation, and drop scheduling
- **Follow Service**: Handles follow/unfollow relationships using sharded databases
- **Order Service**: Processes transactions with inventory management and idempotency guarantees
- **Notification Service**: Coordinates real-time alerts through SSE connections
- **Payment Service**: Integrates with external payment providers

#### 4. Data Layer
- **Sharded Databases**: Follow data is partitioned across multiple database instances using creator_id-based sharding
- **Redis Cache**: Provides low-latency access to frequently requested data and atomic inventory operations
- **IndexedDB**: Client-side storage for offline functionality and improved user experience

#### 5. Event System
- **Pub/Sub Messaging**: Enables asynchronous communication between services
- **Event-Driven Architecture**: Services publish and subscribe to events for decoupled operations
- **Real-Time Updates**: Stock changes, new drops, and order status updates propagate through events

### Data Flow Patterns

1. **Read Operations**: Client → API Gateway → Service → Cache → Database (if cache miss)
2. **Write Operations**: Client → API Gateway → Service → Database → Cache Invalidation → Event Publication
3. **Real-Time Notifications**: Event → Pub/Sub → Notification Service → SSE → Client
4. **External Integrations**: Service → External Payment Provider → Callback Handler

### Key Design Features

- **Horizontal Scaling**: Stateless services can be scaled independently based on load
- **Database Sharding**: Follows table partitioned to prevent celebrity creator bottlenecks
- **Caching Strategy**: Hybrid approach using Cache-Aside with TTL for most data and explicit invalidation for critical inventory data
- **Idempotent Operations**: Client-generated keys prevent duplicate orders during retries
- **Eventual Consistency**: Acceptable for social features while maintaining strong consistency for transactions

### Resilience Patterns
- **Health Monitoring**: Comprehensive metrics collection for all system components

