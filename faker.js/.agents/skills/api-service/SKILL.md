# api service

## Description
This skill is responsible for creating API endpoints for the application. It consists of step by step process of maintaining and creating new API endpoints and maintaining patterns, best practices while creating endpoints.

## When to use
- Trigger when the user asks to create/update API endpoints for the application.
- Trigger when the user asks to remove endpoints from the application.

## Inputs
- `base api endpoint` (/api/v1/): Base api endpoint of the application.
- `/docs/API_SPEC.md`: API specification file, that has information about all the api routes and api request and response skeleton.
- `/docs/DB_SCHEMA.md`: Database schema file, that has information about all the database tables.
- `./agents/workflows/api-service.agent.md`: API service workflow file, that has information about all the api service workflow.

## Steps
1. **Analyze the Request**: Analyze the request of the user and check whether that exists on the API spec or not.
2. **Create a Detailed Plan**: Create a detailed plan that consists of file names, service logics, folders/files to update, and files to create.
3. **Reference Database Schema**: Refer to the DB schema and get to know about the fields, create type interfaces based on what is needed, and follow the response and request body pattern in the `API_SPEC.md` as well.
4. **Follow Rules & Workflows**: Continue as per the rules and workflows and don't break them. If confused, refer to another API route that already exists.
5. **Extract Zod Validations**: Put Zod validation schemas in a separate file within the `src/validation/` folder and import them into the controllers for request validation.

## Examples
### Workflow-Compliant API Stack Example (`order` entity)

#### 1. Generate Types
**File**: `src/@types/order.ts`
```typescript
import { Order } from '@prisma/client';

export interface CreateOrderRequest {
  productId: string;
  quantity: number;
}

export interface OrderResponse {
  success: boolean;
  data?: Order;
  error?: string;
}
```

#### 2. Create Service logic
**File**: `src/services/order-service.ts`
```typescript
import { prisma } from '../lib/prisma';
import { CreateOrderRequest } from '../@types/order';

export async function createOrder(data: CreateOrderRequest) {
  // Business logic here
  return await prisma.order.create({
    data: {
      productId: data.productId,
      quantity: data.quantity,
    },
  });
}
```

#### 3. Create Helpers (if needed)
**File**: `src/helpers/order-helper.ts`
```typescript
// Pure, generic functions for formatting or calculations
export function formatOrderAmount(amount: number): string {
  return `$${amount.toFixed(2)}`;
}
```

#### 4. Create Controller
**File**: `src/controllers/order-controller.ts`
```typescript
import { Request, Response } from 'express';
import * as orderService from '../services/order-service';

export async function createOrderHandler(req: Request, res: Response) {
  try {
    const result = await orderService.createOrder(req.body);
    return res.status(201).json({
      success: true,
      data: result,
    });
  } catch (error: any) {
    return res.status(500).json({
      success: false,
      error: error.message || 'Internal server error',
    });
  }
}
```

#### 5. Route
**File**: `src/routes/order-routes.ts`
```typescript
import { Router } from 'express';
import { createOrderHandler } from '../controllers/order-controller';

const router = Router();

router.post('/', createOrderHandler);

export default router;
```